import json
class Expense:
    Total=0
    def __init__(self,date, category, amount, description):
        self.date = date 
        self.category = category
        self.amount = amount
        self.description = description
        Expense.Total+=amount  
    def convertdict(self):
        mydic={
            "date":self.date,
            "category":self.category,
            "amount":self.amount,
            "description":self.description
        }
        return mydic 
    def Totalexpenses():
        return Expense.Total
new_expense=Expense("12-04-2026","Travel",2500,"Trip to Vizag")
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
print(type(data))
tot=0
for expense in data["Harsha"]:
    print(expense)
    tot+=expense["amount"]
print("Final Expense:",tot)


