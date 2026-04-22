import tkinter as tk
from notes import AiAnalysis
from analysis import ShowGraphs
from analysis import MaxspentCategory,maxbudget,LowspentCategory,minbudget,lowest,highest
from main import RunInput

mywindow=tk.Tk()
mywindow.title("Mind Spend")

MaxExpenseLabel=tk.Label(mywindow,text=f"Highest Expense: Rs.{highest}")
MaxExpenseLabel.grid(row=0,column=0)
MinExpenseLabel=tk.Label(mywindow,text=f"Lowest Expense: Rs.{lowest}")
MinExpenseLabel.grid(row=0,column=1)
MaxBudgetlabel=tk.Label(mywindow,text=f"Top Spending Category: {MaxspentCategory} : Rs.{maxbudget}")
MaxBudgetlabel.grid(row=1,column=0)
MinBudgetlabel=tk.Label(mywindow,text=f"Least Spending Category: {LowspentCategory} : Rs.{minbudget}")
MinBudgetlabel.grid(row=1,column=1)
AiLabel=tk.Label(mywindow,text=AiAnalysis,wraplength=350)
AiLabel.grid(row=2,column=0,columnspan=2)
AnalysisButton=tk.Button(mywindow,text="Analysis",command=ShowGraphs)
AnalysisButton.grid(row=3,column=1)
# Four Labels to be displayed when Add Expense is clicked 
dateLabel=tk.Label(mywindow,text="Date (DD-MM-YYYY)")
categoryLabel=tk.Label(mywindow,text="Category")
amountLabel=tk.Label(mywindow,text="Price")
descLabel=tk.Label(mywindow,text="Description")

dateEntry=tk.Entry(mywindow)
categoryVar=tk.StringVar(mywindow)
categoryVar.set("Food")
categoryMenu=tk.OptionMenu(mywindow,categoryVar,"Food","Travel","Shopping","Bills","Entertainment")
amountEntry=tk.Entry(mywindow)
descEntry=tk.Entry(mywindow)

def AddExpense():
    RunInput(dateEntry.get(),categoryVar.get(),amountEntry.get(),descEntry.get())
    dateLabel.grid_remove()
    dateEntry.grid_remove()
    categoryLabel.grid_remove()
    categoryMenu.grid_remove()
    amountLabel.grid_remove()
    amountEntry.grid_remove()
    descLabel.grid_remove()
    descEntry.grid_remove()
    finalAddBtn.grid_remove()

def ShowInputs():
    dateLabel.grid(row=4,column=0)
    dateEntry.grid(row=4,column=1)
    categoryLabel.grid(row=5,column=0)
    categoryMenu.grid(row=5,column=1)
    amountLabel.grid(row=6,column=0)
    amountEntry.grid(row=6,column=1)
    descLabel.grid(row=7,column=0)
    descEntry.grid(row=7,column=1)
    finalAddBtn.grid(row=8,column=0,columnspan=2)

AddExpensebtn=tk.Button(mywindow,text="Add Expense",command=ShowInputs)
AddExpensebtn.grid(row=3,column=0)

finalAddBtn=tk.Button(mywindow,text="Add",command=AddExpense)

mywindow.mainloop()