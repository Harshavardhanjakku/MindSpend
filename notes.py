from openai import OpenAI
import os
from dotenv import load_dotenv
import json
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
with open("myexpenses.json") as f:
    data=json.load(f)
response = client.responses.create(
    input=str(data) +"Conclusion in One line about my budget to save money",
    model="openai/gpt-oss-20b",
)

print(response.output_text)