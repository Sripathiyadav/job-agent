from job_search import search_jobs
from database import get_job_by_id, save_job

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from database import (
    get_job_by_id,
    save_job,
    get_saved_jobs
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


async def details(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage: /details 1"
        )
        return

    try:
        job_id = int(context.args[0])

        job = get_job_by_id(job_id)

        if not job:
            await update.message.reply_text(
                "Job not found."
            )
            return

        message = (
            f"📌 Job ID: {job[0]}\n\n"
            f"💼 Title: {job[1]}\n"
            f"🏢 Company: {job[2]}\n"
            f"📍 Location: {job[3]}\n"
            f"🌐 Source: {job[5]}\n"
            f"🔗 URL:\n{job[4]}"
        )

        await update.message.reply_text(message)

    except ValueError:
        await update.message.reply_text(
            "Please provide a valid job number."
        )

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


async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage: /save 1"
        )
        return

    try:
        job_id = int(context.args[0])

        job = get_job_by_id(job_id)

        if not job:
            await update.message.reply_text(
                "Job not found."
            )
            return

        save_job(
            update.effective_user.id,
            job_id
        )

        await update.message.reply_text(
            f"✅ Saved job #{job_id}"
        )

    except ValueError:
        await update.message.reply_text(
            "Please provide a valid job number."
        )


async def saved(update: Update, context: ContextTypes.DEFAULT_TYPE):

    jobs = get_saved_jobs(
        update.effective_user.id
    )

    if not jobs:
        await update.message.reply_text(
            "No saved jobs."
        )
        return

    message = "📌 Saved Jobs\n\n"

    for job in jobs:
        message += (
            f"{job[0]}. {job[1]} - {job[2]}\n"
        )

    await update.message.reply_text(message)


app = Application.builder().token(
    TELEGRAM_TOKEN
).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jobs", jobs))
app.add_handler(CommandHandler("details", details))
app.add_handler(CommandHandler("save", save))
app.add_handler(CommandHandler("saved", saved))


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)

print("AgentClaw AI Started...")

app.run_polling()