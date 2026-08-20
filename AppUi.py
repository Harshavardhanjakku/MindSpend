import tkinter as tk
from notes import AiAnalysis
from analysis import ShowGraphs
from analysis import MaxspentCategory, maxbudget, LowspentCategory, minbudget, lowest, highest
from main import RunInput

mywindow = tk.Tk()
mywindow.title("Mind Spend")

# ---- Top Stats ----
MaxExpenseLabel = tk.Label(mywindow, text=f"Highest Expense: Rs.{highest}")
MaxExpenseLabel.grid(row=0, column=0)

MinExpenseLabel = tk.Label(mywindow, text=f"Lowest Expense: Rs.{lowest}")
MinExpenseLabel.grid(row=0, column=1)

MaxBudgetlabel = tk.Label(
    mywindow,
    text=f"Top Spending Category: {MaxspentCategory} : Rs.{maxbudget}"
)
MaxBudgetlabel.grid(row=1, column=0)

MinBudgetlabel = tk.Label(
    mywindow,
    text=f"Least Spending Category: {LowspentCategory} : Rs.{minbudget}"
)
MinBudgetlabel.grid(row=1, column=1)

# ---- AI Insight ----
AiLabel = tk.Label(mywindow, text=AiAnalysis, wraplength=350)
AiLabel.grid(row=2, column=0, columnspan=2)

# ---- Buttons ----
AnalysisButton = tk.Button(mywindow, text="Analysis", command=ShowGraphs)
AnalysisButton.grid(row=3, column=1)

AddExpensebtn = tk.Button(mywindow, text="Add Expense", command=lambda: ShowInputs())
AddExpensebtn.grid(row=3, column=0)

# ---- Input Fields ----
dateLabel = tk.Label(mywindow, text="Date (DD-MM-YYYY)")
categoryLabel = tk.Label(mywindow, text="Category")
amountLabel = tk.Label(mywindow, text="Price")
descLabel = tk.Label(mywindow, text="Description")

dateEntry = tk.Entry(mywindow)

categoryVar = tk.StringVar(mywindow)
categoryVar.set("Food")

categoryMenu = tk.OptionMenu(
    mywindow,
    categoryVar,
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Entertainment"
)

amountEntry = tk.Entry(mywindow)
descEntry = tk.Entry(mywindow)

# ---- Functions ----
def AddExpense():
    RunInput(
        dateEntry.get(),
        categoryVar.get(),
        amountEntry.get(),
        descEntry.get()
    )

    # Simple refresh (restart UI)
    mywindow.destroy()
    import appui


def ShowInputs():
    dateLabel.grid(row=4, column=0)
    dateEntry.grid(row=4, column=1)

    categoryLabel.grid(row=5, column=0)
    categoryMenu.grid(row=5, column=1)

    amountLabel.grid(row=6, column=0)
    amountEntry.grid(row=6, column=1)

    descLabel.grid(row=7, column=0)
    descEntry.grid(row=7, column=1)

    finalAddBtn.grid(row=8, column=0, columnspan=2)


# ---- Final Add Button ----
finalAddBtn = tk.Button(mywindow, text="Add", command=AddExpense)

# ---- Run ----
mywindow.mainloop()