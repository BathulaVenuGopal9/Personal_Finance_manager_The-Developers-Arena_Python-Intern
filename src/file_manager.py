import csv
import os
import shutil
from datetime import datetime
from src.expense import Expense


FILE_PATH = "data/expenses.csv"


# -------------------------------
# LOAD EXPENSES FROM CSV
# -------------------------------
def load_expenses():
    expenses = []

    if not os.path.exists(FILE_PATH):
        return expenses

    with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header

        for row in reader:
            if row:
                date, category, amount, description = row
                expenses.append(Expense(amount, category, date, description))

    return expenses


# -------------------------------
# SAVE EXPENSES TO CSV
# -------------------------------
def save_expenses(expenses):
    with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

        for exp in expenses:
            writer.writerow(exp.to_list())


# -------------------------------
# BACKUP DATA
# -------------------------------
def backup_data():
    if not os.path.exists(FILE_PATH):
        print("No data file found to backup.")
        return

    if not os.path.exists("backups"):
        os.makedirs("backups")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backups/expenses_backup_{timestamp}.csv"

    shutil.copy(FILE_PATH, backup_file)
    print(f"✅ Backup created successfully → {backup_file}")


# -------------------------------
# RESTORE DATA
# -------------------------------
def restore_data():
    if not os.path.exists("backups"):
        print("No backups available.")
        return

    files = os.listdir("backups")

    if not files:
        print("No backup files found.")
        return

    print("\nAvailable Backups:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")

    choice = input("Select backup number to restore: ")

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(files):
        print("❌ Invalid selection.")
        return

    selected_file = files[int(choice) - 1]
    backup_path = os.path.join("backups", selected_file)

    shutil.copy(backup_path, FILE_PATH)
    print("✅ Data restored successfully!")

