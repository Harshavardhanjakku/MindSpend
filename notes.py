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
monthly_expenses = {
    "Jan": 1200,
    "Feb": 950,
    "Mar": 2300,
    "Apr": 1800,
    "May": 2100,
    "Jun": 1600,
    "Jul": 2000,
    "Aug": 1750,
    "Sep": 1900,
    "Oct": 2200,
    "Nov": 2500,
    "Dec": 3000
}
with open("myexpenses.json") as f:
    data=json.load(f)
montlydata = client.responses.create(
    input=str(monthly_expenses) +"I want only dictonary just like the attached montly expenses no ** nothing"+str(data),
    model="openai/gpt-oss-20b",
)
print(montlydata.output_text)
print(response.output_text)