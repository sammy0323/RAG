"""
Test OpenAI API Key
"""
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {api_key[:20]}..." if api_key else "No API key found")

if api_key:
    from openai import OpenAI
    
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello from RAG System'"}],
            max_tokens=50
        )
        print(f"\n✅ API Key is valid!")
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"\n❌ API Error: {str(e)}")
else:
    print("❌ No API key found in .env")
