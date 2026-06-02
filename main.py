from job_search import search_jobs
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import requests
from config import TELEGRAM_TOKEN

# Memory store
user_memories = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "AgentClaw AI Online 🚀"
    )


async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text(
            "Usage: /jobs flutter"
        )
        return

    jobs_found = search_jobs(query)

    message = "🔍 Job Results\n\n"

    for i, job in enumerate(jobs_found, start=1):
        message += (
            f"{i}. {job['title']}\n"
            f"📍 {job['location']}\n\n"
        )

    await update.message.reply_text(message)


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    print(f"Received: {user_message}")

    if user_id not in user_memories:
        user_memories[user_id] = []

    user_memories[user_id].append(
        {
            "role": "user",
            "content": user_message
        }
    )

    recent_messages = user_memories[user_id][-20:]

    print("MEMORY:")
    for msg in recent_messages:
        print(msg)

    try:
        print("Sending request to Ollama...")

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "qwen2.5:1.5b",
                "messages": recent_messages,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()

        ai_reply = response.json()["message"]["content"]

        print("Ollama response received")
        print(f"Reply: {ai_reply}")

        user_memories[user_id].append(
            {
                "role": "assistant",
                "content": ai_reply
            }
        )

        await update.message.reply_text(ai_reply)

    except Exception as e:
        print("ERROR:", str(e))
        await update.message.reply_text(
            f"Error: {str(e)}"
        )


app = Application.builder().token(
    TELEGRAM_TOKEN
).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jobs", jobs))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)

print("AgentClaw AI Started...")

app.run_polling()