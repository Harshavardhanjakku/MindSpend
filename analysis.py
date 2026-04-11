import json
categories={"Food":0,"Travel":0,"Shopping":0,"Bills":0,"Entertainment":0}

with open("myexpenses.json") as f :
    data=json.load(f)
    for expense in data :
        x=expense['category']
        categories[x]+=expense['amount']
print(categories)

