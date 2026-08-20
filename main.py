import json

def RunInput(date, category, price, description):

    category = category.title()
    price = int(price)

    with open("MyExpenses.json") as f:
        data = json.load(f)

    new_expense = {
        "date": date,
        "category": category,
        "amount": price,
        "description": description
    }

    data.append(new_expense)

    with open("MyExpenses.json", "w") as f:
        json.dump(data, f, indent=4)