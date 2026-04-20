import json
import matplotlib.pyplot as plt

categories = {"Food":0,"Travel":0,"Shopping":0,"Bills":0,"Entertainment":0}
mycolors = ["blue","pink","green","yellow","purple"]

lowest = float('inf')
highest = float('-inf')
flag = False

with open("myexpenses.json") as f:
    data = json.load(f)

    if len(data) == 0:
        lowest = None
        highest = None
        flag = True
    else:
        for expense in data:
            lowest = min(lowest, expense['amount'])
            highest = max(highest, expense['amount'])
            categories[expense['category']] += expense['amount']

def ChangeFormat(x):
    d, m, y = map(int, x["date"].split("-"))
    return (y, m, d)

sorted_expenses = sorted(data, key=ChangeFormat)

dates = [i["date"] for i in sorted_expenses]
amounts = [i["amount"] for i in sorted_expenses]

fig, axis = plt.subplots(2,2, figsize=(10,8))

axis[0,0].axis('off')

if not flag:
    SortedCategory = sorted(categories, key=lambda x: categories[x], reverse=True)
    MaxspentCategory = SortedCategory[0]
    LowspentCategory = SortedCategory[-1]

    text = f"""
📊 Analysis

Highest: {MaxspentCategory} (Rs.{categories[MaxspentCategory]})
Lowest: {LowspentCategory} (Rs.{categories[LowspentCategory]})

Min Expense: Rs.{lowest}
Max Expense: Rs.{highest}
"""
else:
    text = "No Data Available"

axis[0,0].text(0.5, 0.5, text, fontsize=20, ha='center', va='center')

if not flag:
    axis[0,1].pie(categories.values(), labels=categories.keys(),
                  colors=mycolors, autopct='%1.1f%%')
    axis[0,1].set_title("Pie Chart")

axis[1,0].plot(dates[-10:], amounts[-10:])
axis[1,0].tick_params(axis='x', rotation=80)
axis[1,0].set_title("Last 10 Days")

axis[1,1].bar(categories.keys(), categories.values(), color=mycolors)
axis[1,1].set_title("Bar Graph")

plt.tight_layout()
plt.show()
