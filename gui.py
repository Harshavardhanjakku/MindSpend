import tkinter as tk
from tkinter import messagebox
from expense import (
    add_expense,
    get_highest,
    get_lowest,
    get_top_category,
    get_low_category,
)
from ai_insight import fetch_ai_insight
from charts import show_charts

CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Entertainment"]
ACCENT = "#4a90d9"
BG = "#f7f9fc"
CARD = "#ffffff"
TEXT = "#1a1a2e"
MUTED = "#6b7280"


# ── Helpers ──────────────────────────────────────────────────────────────────

def styled_label(parent, text, bold=False, muted=False, size=10):
    return tk.Label(
        parent,
        text=text,
        bg=CARD,
        fg=MUTED if muted else TEXT,
        font=("Helvetica", size, "bold" if bold else "normal"),
    )


def styled_entry(parent):
    e = tk.Entry(parent, relief="flat", bg="#eef2f7", fg=TEXT, font=("Helvetica", 10))
    e.config(highlightthickness=1, highlightbackground="#d1d5db", highlightcolor=ACCENT)
    return e


def card_frame(parent, **kw):
    return tk.Frame(parent, bg=CARD, relief="flat", bd=0, **kw)


# ── Dashboard refresh ─────────────────────────────────────────────────────────

def refresh_dashboard(labels: dict) -> None:
    top_cat, top_amt = get_top_category()
    low_cat, low_amt = get_low_category()
    labels["highest"].config(text=f"Rs. {get_highest()}")
    labels["lowest"].config(text=f"Rs. {get_lowest()}")
    labels["top_cat"].config(text=f"{top_cat}  •  Rs. {top_amt}")
    labels["low_cat"].config(text=f"{low_cat}  •  Rs. {low_amt}")


# ── Add Expense form ──────────────────────────────────────────────────────────

def build_form(parent, dashboard_labels: dict) -> tk.Frame:
    form = card_frame(parent, padx=16, pady=12)

    styled_label(form, "Add Expense", bold=True, size=11).grid(
        row=0, column=0, columnspan=2, sticky="w", pady=(0, 8)
    )

    fields = {}
    rows = [
        ("date", "Date (DD-MM-YYYY)"),
        ("amount", "Amount (Rs.)"),
        ("desc", "Description"),
    ]
    for i, (key, label) in enumerate(rows, start=1):
        styled_label(form, label, muted=True).grid(row=i, column=0, sticky="w", pady=3)
        entry = styled_entry(form)
        entry.grid(row=i, column=1, sticky="ew", padx=(8, 0), pady=3)
        fields[key] = entry

    styled_label(form, "Category", muted=True).grid(row=4, column=0, sticky="w", pady=3)
    cat_var = tk.StringVar(value=CATEGORIES[0])
    cat_menu = tk.OptionMenu(form, cat_var, *CATEGORIES)
    cat_menu.config(bg=CARD, relief="flat", font=("Helvetica", 10))
    cat_menu.grid(row=4, column=1, sticky="ew", padx=(8, 0), pady=3)

    status = styled_label(form, "", muted=True)
    status.grid(row=6, column=0, columnspan=2, pady=(4, 0))

    def submit():
        date = fields["date"].get().strip()
        amount = fields["amount"].get().strip()
        desc = fields["desc"].get().strip()
        category = cat_var.get()

        if not (date and amount and desc):
            status.config(text="All fields are required.", fg="red")
            return
        if not amount.isdigit():
            status.config(text="Amount must be a number.", fg="red")
            return

        add_expense(date, category, amount, desc)
        for e in fields.values():
            e.delete(0, tk.END)
        status.config(text="Expense saved.", fg="green")
        refresh_dashboard(dashboard_labels)

    tk.Button(
        form,
        text="Save Expense",
        command=submit,
        bg=ACCENT,
        fg="white",
        relief="flat",
        font=("Helvetica", 10, "bold"),
        cursor="hand2",
        padx=12,
        pady=6,
    ).grid(row=5, column=0, columnspan=2, sticky="ew", pady=(10, 0))

    form.columnconfigure(1, weight=1)
    return form


# ── Main window ───────────────────────────────────────────────────────────────

def launch() -> None:
    win = tk.Tk()
    win.title("Mind Spend")
    win.configure(bg=BG)
    win.resizable(False, False)

    top_cat, top_amt = get_top_category()
    low_cat, low_amt = get_low_category()
    insight = fetch_ai_insight()

    # ── Header ────────────────────────────────────────────────────────────────
    header = tk.Frame(win, bg=ACCENT, padx=20, pady=14)
    header.pack(fill="x")
    tk.Label(
        header,
        text="Mind Spend",
        bg=ACCENT,
        fg="white",
        font=("Helvetica", 18, "bold"),
    ).pack(side="left")

    # ── Stats row ─────────────────────────────────────────────────────────────
    stats_row = tk.Frame(win, bg=BG, padx=16, pady=12)
    stats_row.pack(fill="x")

    dashboard_labels = {}

    stat_defs = [
        ("highest", "Highest Expense", f"Rs. {get_highest()}"),
        ("lowest",  "Lowest Expense",  f"Rs. {get_lowest()}"),
        ("top_cat", "Top Category",    f"{top_cat}  •  Rs. {top_amt}"),
        ("low_cat", "Least Category",  f"{low_cat}  •  Rs. {low_amt}"),
    ]

    for col, (key, title, value) in enumerate(stat_defs):
        cell = card_frame(stats_row, padx=12, pady=10)
        cell.grid(row=0, column=col, padx=6, sticky="nsew")
        styled_label(cell, title, muted=True, size=9).pack(anchor="w")
        val_lbl = styled_label(cell, value, bold=True, size=11)
        val_lbl.pack(anchor="w", pady=(2, 0))
        dashboard_labels[key] = val_lbl

    stats_row.columnconfigure(list(range(4)), weight=1)

    # ── AI Insight ────────────────────────────────────────────────────────────
    insight_card = card_frame(win, padx=16, pady=12)
    insight_card.pack(fill="x", padx=16, pady=(0, 8))
    styled_label(insight_card, "AI Insight", bold=True, size=10).pack(anchor="w")
    tk.Label(
        insight_card,
        text=insight,
        bg=CARD,
        fg=MUTED,
        font=("Helvetica", 10),
        wraplength=520,
        justify="left",
    ).pack(anchor="w", pady=(4, 0))

    # ── Form + Analysis button ────────────────────────────────────────────────
    bottom = tk.Frame(win, bg=BG, padx=16, pady=0)
    bottom.pack(fill="x", pady=(0, 16))

    form = build_form(bottom, dashboard_labels)
    form.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

    side = card_frame(bottom, padx=16, pady=12)
    side.grid(row=0, column=1, sticky="nsew")
    styled_label(side, "Reports", bold=True, size=11).pack(anchor="w", pady=(0, 8))
    tk.Button(
        side,
        text="View Charts",
        command=show_charts,
        bg=ACCENT,
        fg="white",
        relief="flat",
        font=("Helvetica", 10, "bold"),
        cursor="hand2",
        padx=12,
        pady=6,
    ).pack(fill="x")

    bottom.columnconfigure(0, weight=3)
    bottom.columnconfigure(1, weight=1)

    win.mainloop()
