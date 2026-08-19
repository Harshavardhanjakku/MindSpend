import json

DB = "expenses.json"


def load() -> list:
    with open(DB) as f:
        return json.load(f)


def save(records: list) -> None:
    with open(DB, "w") as f:
        json.dump(records, f, indent=4)


def append_record(record: dict) -> None:
    records = load()
    records.append(record)
    save(records)
