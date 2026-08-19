import os
from openai import OpenAI
from dotenv import load_dotenv
from Assignments.MindSpend.storage import load

load_dotenv()


def fetch_ai_insight() -> str:
    try:
        client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
        )
        data = load()
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": f"{data} Give a one-line budget insight to help save money.",
                }
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI insight unavailable: {e}"
