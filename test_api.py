import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5-coder:7b",
        "prompt": "Say hello in one sentence",
        "stream": False
    },
    timeout=120
)

print(response.json()["response"])