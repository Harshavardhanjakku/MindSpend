import matplotlib.pyplot as plt
from Assignments.MindSpend.expense import get_category_totals


def show_charts() -> None:
    totals = get_category_totals()
    if not totals:
        return

    categories = list(totals.keys())
    amounts = list(totals.values())

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Mind Spend — Expense Analysis", fontsize=14, fontweight="bold")

    ax1.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    ax1.set_title("Category Breakdown")

    ax2.bar(categories, amounts, color="#4a90d9")
    ax2.set_title("Spending by Category")
    ax2.set_xlabel("Category")
    ax2.set_ylabel("Amount (Rs.)")
    ax2.tick_params(axis="x", rotation=20)

    plt.tight_layout()
    plt.show()
