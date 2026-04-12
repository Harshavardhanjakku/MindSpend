import json
import matplotlib.pyplot as plt
from datetime import datetime
categories={"Food":0,"Travel":0,"Shopping":0,"Bills":0,"Entertainment":0}
mycolors = [ "blue","pink","green", "yellow",  "purple"]
lowest=float('inf')
highest=float('-inf')
flag=False 
with open("myexpenses.json") as f :
    data=json.load(f)
    if len(data)==0:
        lowest=None 
        highest=None 
        flag=True
    else:
        for expense in data :
            lowest=min(lowest,expense['amount'])
            highest=max(highest,expense['amount'])
            x=expense['category']
            categories[x]+=expense['amount']
print(categories)
print(f"Lowest:{lowest} and Highest :{highest}")
def Showpiechart():
    if not flag:
        plt.pie(categories.values(),labels=categories.keys(),colors=mycolors,autopct='%1.1f%%')
        plt.title("Expenses Piechart by category")
        plt.show() 
def ShowBargraph():
    plt.bar(categories.keys(),categories.values(),color=mycolors)
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.show()

Showpiechart()
ShowBargraph()

myfinal = sorted(
    data,
    key=lambda x: datetime.strptime(x["date"], "%d-%m-%Y")
)