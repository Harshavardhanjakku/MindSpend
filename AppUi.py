import tkinter as tk
from notes import AiAnalysis
from analysis import ShowGraphs
from analysis import MaxspentCategory,maxbudget,LowspentCategory,minbudget,lowest,highest
mywindow=tk.Tk()
mywindow.title("Mind Spend")
MaxExpenseLabel=tk.Label(mywindow,text=f"Highest Expense: Rs.{highest}")
MaxExpenseLabel.grid(row=0,column=0)
MinExpenseLabel=tk.Label(mywindow,text=f"Lowest Expense: Rs.{lowest}")
MinExpenseLabel.grid(row=0,column=1)
MaxBudgetlabel = tk.Label(mywindow,text=f"Top Spending Category: {MaxspentCategory} : Rs.{maxbudget}")
MaxBudgetlabel.grid(row=1,column=0)
MinBudgetlabel=tk.Label(mywindow,text=f"Least Spending Category: {LowspentCategory} : Rs.{minbudget}")
MinBudgetlabel.grid(row=1,column=1)
AiLabel = tk.Label(
    mywindow,
    text=AiAnalysis,
    wraplength=350, 
)
AiLabel.grid(row=2, column=0, columnspan=2)
AddExpensebtn=tk.Button(mywindow,text="Add Expense")
AddExpensebtn.grid(row=3,column=0)
AnalysisButton=tk.Button(mywindow,text="Analysis",command=ShowGraphs)
AnalysisButton.grid(row=3,column=1)
mywindow.mainloop()
