import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PPLX_API_KEY")

url = "https://api.perplexity.ai/chat/completions"

payload = {
    "model": "llama-3.1-sonar-small-128k-online",
    "messages": [
        {"role": "user", "content": "Hello! Are you working?"}
    ]
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("⏳ Testing connection with User-Agent trick...")
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("✅ SUCCESS! تغلبت على Cloudflare والمفتاح يخدم!")
    print(response.json())
else:
    print(f"❌ ERROR: {response.status_code}")
    print(response.text[:200])