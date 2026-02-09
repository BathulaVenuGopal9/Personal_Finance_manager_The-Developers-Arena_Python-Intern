from src.expense import Expense
from src.file_manager import (
    load_expenses,
    save_expenses,
    backup_data,
    restore_data,
)
from src.menu import show_menu
from src.utils import validate_amount, validate_date
from src.reports import category_summary, monthly_report


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        # ---------------- ADD EXPENSE ----------------
        if choice == "1":
            amount = input("Enter amount: ")
            if not validate_amount(amount):
                print("❌ Invalid amount. Try again.")
                continue

            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("❌ Invalid date format.")
                continue

            description = input("Enter description: ")

            expense = Expense(float(amount), category, date, description)
            expenses.append(expense)
            save_expenses(expenses)

            print("✅ Expense added successfully!")

        # ---------------- VIEW ALL ----------------
        elif choice == "2":
            if not expenses:
                print("No expenses found.")
            else:
                print("\nAll Expenses:")
                for exp in expenses:
                    print(exp)

        # ---------------- CATEGORY SUMMARY ----------------
        elif choice == "3":
            category_summary(expenses)

        # ---------------- MONTHLY REPORT ----------------
        elif choice == "4":
            monthly_report(expenses)

        # ---------------- BACKUP DATA ----------------
        elif choice == "5":
            backup_data()

        # ---------------- RESTORE DATA ----------------
        elif choice == "6":
            restore_data()
            expenses = load_expenses()  # Reload after restore

        # ---------------- EXIT ----------------
        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()


