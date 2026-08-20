import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

AiAnalysis = "No AI insight available."

try: 
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file") 
    client = Groq(api_key=api_key) 
    with open("MyExpenses.json", "r", encoding="utf-8") as f:
        data = json.load(f) 
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a personal finance assistant for the MindSpend app. "
                    "Analyze the user's expenses and provide one short, practical "
                    "money-saving tip. Keep the answer simple and under 2 sentences."
                )
            },
            {
                "role": "user",
                "content": f"Here are my expenses:\n{json.dumps(data, indent=2)}"
            }
        ],
        max_tokens=100
    ) 
    AiAnalysis = response.choices[0].message.content

    print("AI INSIGHT:")
    print(AiAnalysis)

except Exception as e:
    print("FULL ERROR:", e)
    AiAnalysis = "Unable to generate AI insight."