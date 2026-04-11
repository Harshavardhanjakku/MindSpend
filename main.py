import json
import tkinter as tk
from tkinter import filedialog
import shutil
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
def Add_Expense():
    new_expense=Expense("28-06-2026","Shopping",3000,"Furinture shopping").convertdict()
    with open("myexpenses.json") as f:
        data = json.load(f) 
    data.append(new_expense)
    with open("myexpenses.json","w") as f:
        json.dump(data,f,indent=4)

window= tk.Tk()
def SaveFile():
    filepath = filedialog.asksaveasfilename(
        defaultextension='.json',
        filetypes=[("JSON file", "*.json"), ("All files", "*.*")]
    )
    if filepath:
        shutil.copy("myexpenses.json", filepath)
downloadbutton=tk.Button(text="save",command=SaveFile)
downloadbutton.pack()
Add_Expense()
print(Expense.calculate_total())

window.mainloop()