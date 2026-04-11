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
        total=0
        with open("myexpenses.json") as f:
            data = json.load(f)
            for expense in data:
                total+=expense["amount"]
        return total
new_expense=Expense("11-04-2026","Travel",2500,"Trip to Vizag").convertdict()
print(new_expense)
print(Expense.calculate_total())
with open("myexpenses.json","w") as f:
    json.dump(new_expense,f)
