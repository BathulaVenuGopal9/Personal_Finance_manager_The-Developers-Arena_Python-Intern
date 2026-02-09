from collections import defaultdict


def category_summary(expenses):
    summary = defaultdict(float)

    for exp in expenses:
        summary[exp.category] += exp.amount

    print("\nCategory-wise Summary:")
    print("-" * 30)

    if not summary:
        print("No expenses found.")
        return

    for category, total in summary.items():
        print(f"{category} : ₹{total:.2f}")


def monthly_report(expenses):
    monthly = defaultdict(float)

    for exp in expenses:
        month = exp.date[:7]  # YYYY-MM
        monthly[month] += exp.amount

    print("\nMonthly Report:")
    print("-" * 30)

    if not monthly:
        print("No expenses found.")
        return

    for month, total in sorted(monthly.items()):
        print(f"{month} : ₹{total:.2f}")

