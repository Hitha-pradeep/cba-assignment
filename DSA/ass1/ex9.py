# Monthly Expense Analyzer
def analyze_expenses(expenses):
    total = sum(expenses)
    max_expense = max(expenses)
    max_day = expenses.index(max_expense) + 1  # +1 for day number
    average = total / len(expenses)
    above_1000 = sum(1 for e in expenses if e > 1000)
    print("===================================")
    print(f"Expenses (30 days): {expenses}")
    print(f"Total Expenses    : ₹{total}")
    print(f"Maximum Expense   : ₹{max_expense} (Day {max_day})")
    print(f"Average Expense   : ₹{average:.2f}")
    print(f"Days > ₹1000      : {above_1000}")
    print("===================================")
def main():
    expenses = []
    for i in range(30):
        exp = float(input(f"Enter expense for Day {i+1}: "))
        expenses.append(exp)
    analyze_expenses(expenses)
if __name__ == "__main__":
    main()
