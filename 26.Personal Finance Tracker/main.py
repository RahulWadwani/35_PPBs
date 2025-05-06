# Global list to store transactions
transactions = []

def transaction():
    print("Add Transaction")
    in_exp = input("Enter income or expense (i/e): ").strip().lower()
    amt = float(input("Enter amount: "))
    cat = input("Enter category: ").strip()
    des = input("Enter description: ").strip()

    transaction = {
        "type": "income" if in_exp == "i" else "expense",
        "amount": amt,
        "category": cat,
        "description": des
    }
    transactions.append(transaction)
    print("Transaction added successfully!")    


def view_transactions():
    if not transactions:
        print("No transactions to display.")
        return

    print("\nAll Transactions:")
    for t in transactions:
        print(f"{t['type'].title():<8} ₹{t['amount']:<10.2f} Category: {t['category']}, Description: {t['description']}")

def summary():
    print("\nFinancial Summary")
    Incomes = sum(t["amount"] for t in transactions if t["type"] == "income")
    Expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    net = Incomes - Expenses
    print(f"Income      : ₹ {Incomes:.2f}")
    print(f"Expenses    : ₹ {Expenses:.2f}")
    print(f"Net Balance : ₹ {net:.2f}")

def main():
    again = True
    while again:
        print("="*40)
        print("==== Personal Finance Tracker ====")
        print("="*40)
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Summary")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        match choice:
            case 1:
                transaction()
            case 2:
                view_transactions()
            case 3:
                summary()
            case 4:
                print("Thank you for using the Personal Finance Tracker!")
                break
            case _:
                print("Invalid choice. Please try again.")

        input_ = input("Do you want to continue? (y/n): ").strip().lower()
        if input_ == 'n':
            again = False
            print("Thank you for using the Personal Finance Tracker!")
        elif input_ != 'y':
            print("Invalid input. Exiting...")
            break

if __name__ == "__main__":
    main()
