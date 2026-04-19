import json
class Expense: 
    def __init__(self,date, category, amount, description):
        self.date = date 
        self.category = category
        self.amount = amount
        self.description = description 
    def convertdict(self):
        mydic={
            "date":self.date,
            "category":self.category,
            "amount":self.amount,
            "description":self.description
        }
        return mydic  
    def calculate_total():
        total = 0
        with open("myexpenses.json") as f:
            data = json.load(f)
            for expense in data:
                total += expense["amount"]
        return total
def Add_Expense(date,category,price,description):
    new_expense=Expense(date,category,price,description).convertdict()
    with open("myexpenses.json") as f:
        data = json.load(f) 
    data.append(new_expense)
    with open("myexpenses.json","w") as f:
        json.dump(data,f,indent=4)
date=input("Enter the Date in format (DD-MM-YYYY) :")
category=input("Enter the Category (Food, Travel, Shopping, Bills, Entertainment) :")
category=category.lower()
category=category.title()
price=int(input("Enter the amount :"))
description=input("Enter the description :")
Add_Expense(date,category,price,description)
print(Expense.calculate_total())
