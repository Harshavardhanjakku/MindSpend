import json

expenses = """
{
    "Harsha": [
        {
            "date": "22-06-2004",
            "amount": 2150,
            "category": "Food",
            "description": "Biryani and Colddrinks"
        },
        {
            "date": "28-06-2024",
            "amount": 1250,
            "category": "Clothing",
            "description": "Dresses and Trousers"
        }
    ]
}
"""

data = json.loads(expenses)

tot=0
for expense in data["Harsha"]:
    print(expense)
    tot+=expense["amount"]
print("Final Expense:",tot)