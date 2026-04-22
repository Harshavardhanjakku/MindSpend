import json
import matplotlib.pyplot as plt 

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

def ChangeFormat(x):
    d, m, y = map(int, x["date"].split("-"))
    return (y, m, d)

sorted_expenses= sorted(data, key=ChangeFormat)
dates=[]
amounts=[]
for i in sorted_expenses:
    dates.append(i["date"])
    amounts.append(i["amount"])

numberofdays=10

def ShowGraphs():
    fig,axis = plt.subplots(2,2)
    axis[0,0].axis('off')
    axis[0,0].text(0.5,0.5,f"Lowest: {lowest}\nHighest: {highest}",ha='center')
    plt.sca(axis[0,1])
    if not flag:
        plt.pie(categories.values(),labels=categories.keys(),colors=mycolors,autopct='%1.1f%%')
    plt.sca(axis[1,0])
    plt.plot(dates[-numberofdays:],amounts[-numberofdays:])
    plt.xticks(rotation=80)
    plt.sca(axis[1,1])
    plt.bar(categories.keys(),categories.values(),color=mycolors)
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")

    plt.show()

SortedCategory=sorted(categories, key=lambda x: categories[x],reverse=True)
MaxspentCategory=SortedCategory[0]
maxbudget=categories[MaxspentCategory]
LowspentCategory=SortedCategory[-1]
minbudget=categories[LowspentCategory]