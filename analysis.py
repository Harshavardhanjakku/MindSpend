import json
import matplotlib.pyplot as plt
categories={"Food":0,"Travel":0,"Shopping":0,"Bills":0,"Entertainment":0}
mycolors = [ "blue","pink","green", "yellow",  "purple"]
with open("myexpenses.json") as f :
    data=json.load(f)
    for expense in data :
        x=expense['category']
        categories[x]+=expense['amount']
print(categories)
plt.pie(categories.values(),labels=categories.keys(),colors=mycolors,autopct='%1.1f%%')
plt.show()