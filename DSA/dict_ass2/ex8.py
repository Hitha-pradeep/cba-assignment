def add_account(accounts, acc_no, name, balance=0):
    accounts[acc_no] = {"name": name, "balance": balance}
    print(f"Account {acc_no} created for {name} with balance ₹{balance}.")
def search_account(accounts, acc_no):
    if acc_no in accounts:
        print(f"Account No: {acc_no}, Name: {accounts[acc_no]['name']}, Balance: ₹{accounts[acc_no]['balance']}")
    else:
        print(f"Account {acc_no} not found.")
def deposit(accounts, acc_no, amount):
    if acc_no in accounts:
        accounts[acc_no]["balance"] += amount
        print(f"₹{amount} deposited. New Balance: ₹{accounts[acc_no]['balance']}")
    else:
        print(f"Account {acc_no} not found.")
def withdraw(accounts, acc_no, amount):
    if acc_no in accounts:
        if amount > accounts[acc_no]["balance"]:
            print("Error: Insufficient Balance!")
        else:
            accounts[acc_no]["balance"] -= amount
            print(f"₹{amount} withdrawn. New Balance: ₹{accounts[acc_no]['balance']}")
    else:
        print(f"Account {acc_no} not found.")
def display_accounts(accounts):
    if not accounts:
        print("No accounts available.")
    else:
        print("Bank Accounts Directory:")
        for acc_no, details in accounts.items():
            print(f"Account No: {acc_no}, Name: {details['name']}, Balance: ₹{details['balance']}")
def main():
    accounts = {}
    while True:
        print("\n--- Banking Account Directory ---")
        print("1. Add Account")
        print("2. Search Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Display All Accounts")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            acc_no = input("Enter Account Number: ")
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))
            add_account(accounts, acc_no, name, balance)
        elif choice == 2:
            acc_no = input("Enter Account Number to search: ")
            search_account(accounts, acc_no)
        elif choice == 3:
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter deposit amount: "))
            deposit(accounts, acc_no, amount)
        elif choice == 4:
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw(accounts, acc_no, amount)
        elif choice == 5:
            display_accounts(accounts)
        elif choice == 6:
            print("Exiting Banking Account Directory...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
