# Bank ATM Simulation
class Account:
    def __init__(self, acc_no, holder_name, balance=0):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully. New Balance: ₹{self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. New Balance: ₹{self.balance}")
    def display_balance(self):
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Current Balance: ₹{self.balance}")
account = Account(101, "Hitha", 5000)
while True:
    print("\n--- ATM Menu ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Display Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == 3:
        account.display_balance()
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
