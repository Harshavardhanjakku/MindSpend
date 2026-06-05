from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

AiAnalysis = "Unable to generate AI analysis."

try:

    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    with open("MyExpenses.json") as f:
        data = json.load(f)

    response = client.responses.create(
        input=str(data) + " Conclusion in one line about my budget to save money without using hyphen",
        model="openai/gpt-oss-20b",
    )

    AiAnalysis = response.output_text

except Exception as e:

    AiAnalysis = f"AI Analysis unavailable: {e}"