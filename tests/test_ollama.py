import ollama

response = ollama.chat(
    model='qwen2.5-coder:7b',
    messages=[
        {
            'role': 'user',
            'content': 'Say hello in one sentence'
        }
    ]
)

print(response['message']['content'])