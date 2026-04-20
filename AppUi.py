import tkinter as tk
from notes import AiAnalysis
from analysis import ShowGraphs
from analysis import MaxspentCategory,maxbudget,LowspentCategory,minbudget,lowest,highest
mywindow=tk.Tk()
mywindow.title("Mind Spend")
MaxBudgetlabel=tk.Label(mywindow,text=f"Highest :{MaxspentCategory} (Rs.{maxbudget})")
MaxBudgetlabel.grid(row=0,column=0)
MinBudgetlabel=tk.Label(mywindow,text=f"Lowest :{LowspentCategory} (Rs.{minbudget})")
MinBudgetlabel.grid(row=0,column=1)
AiLabel = tk.Label(
    mywindow,
    text=AiAnalysis,
    wraplength=350, 
)
AiLabel.grid(row=1, column=0, columnspan=2)
AddExpensebtn=tk.Button(mywindow,text="Add Expense")
AddExpensebtn.grid(row=2,column=0)
AnalysisButton=tk.Button(mywindow,text="Analysis",command=ShowGraphs)
AnalysisButton.grid(row=2,column=1)
mywindow.mainloop()
