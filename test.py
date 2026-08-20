import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API KEY FOUND:", bool(api_key))

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Give me one short money saving tip."
        }
    ],
    max_tokens=100
)

print("\nAI RESPONSE:")
print(response.choices[0].message.content)