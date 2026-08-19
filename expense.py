from dataclasses import dataclass, asdict
from Assignments.MindSpend.storage import load, append_record


@dataclass
class Expense:
    date: str
    category: str
    amount: int
    description: str

    def to_dict(self) -> dict:
        return asdict(self)


def add_expense(date: str, category: str, amount: str, description: str) -> None:
    record = Expense(
        date=date,
        category=category.strip().title(),
        amount=int(amount),
        description=description,
    ).to_dict()
    append_record(record)


def get_total() -> int:
    return sum(e["amount"] for e in load())


def get_highest() -> int:
    records = load()
    return max((e["amount"] for e in records), default=0)


def get_lowest() -> int:
    records = load()
    return min((e["amount"] for e in records), default=0)


def get_category_totals() -> dict:
    totals = {}
    for e in load():
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals


def get_top_category() -> tuple:
    totals = get_category_totals()
    if not totals:
        return ("None", 0)
    cat = max(totals, key=totals.get)
    return (cat, totals[cat])


def get_low_category() -> tuple:
    totals = get_category_totals()
    if not totals:
        return ("None", 0)
    cat = min(totals, key=totals.get)
    return (cat, totals[cat])
