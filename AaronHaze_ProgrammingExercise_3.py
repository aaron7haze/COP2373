from functools import reduce

# ---------------------------------------------
# Function: get_expenses
# Description: Collects expense entries from the user until "done" is entered.
# Returns: A list of tuples (expense_type, amount)
# ---------------------------------------------
def get_expenses():
    expenses = []

    while True:
        expense_type = input("Enter expense type (or 'done' to finish): ").strip()

        if expense_type.lower() == "done":
            break

        try:
            amount = float(input(f"Enter amount for {expense_type}: "))
        except ValueError:
            print("Invalid amount. Try again.")
            continue

        expenses.append((expense_type, amount))

    return expenses


# ---------------------------------------------
# Function: calculate_total
# Description: Uses reduce() to compute the total of all expenses.
# Parameters: expenses (list of tuples)
# Returns: float total
# ---------------------------------------------
def calculate_total(expenses):
    return reduce(lambda acc, item: acc + item[1], expenses, 0.0)


# ---------------------------------------------
# Function: find_highest
# Description: Uses reduce() to find the highest expense.
# Parameters: expenses (list of tuples)
# Returns: tuple (expense_type, amount)
# ---------------------------------------------
def find_highest(expenses):
    return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)


# ---------------------------------------------
# Function: find_lowest
# Description: Uses reduce() to find the lowest expense.
# Parameters: expenses (list of tuples)
# Returns: tuple (expense_type, amount)
# ---------------------------------------------
def find_lowest(expenses):
    return reduce(lambda a, b: a if a[1] < b[1] else b, expenses)


# ---------------------------------------------
# Function: main
# Description: Controls program flow and prints results.
# ---------------------------------------------
def main():
    print("Monthly Expense Analyzer")
    print("------------------------")

    expenses = get_expenses()

    if not expenses:
        print("No expenses entered.")
        return

    total = calculate_total(expenses)
    highest = find_highest(expenses)
    lowest = find_lowest(expenses)

    print("\nExpense Summary")
    print("------------------------")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")


# Run the program
if __name__ == "__main__":
    main()
