# Bank Account System
class BankAccount:
    def __init__(self, acc_no, holder_name, balance=0):
        self.__acc_no = acc_no
        self.__holder_name = holder_name
        self.__balance = balance
        self.__transactions = []  # Store transaction history
    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited successfully. New Balance: ₹{self.__balance}")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Error: Insufficient Balance!")
            self.__transactions.append(f"Failed Withdrawal ₹{amount} (Insufficient Balance)")
        else:
            self.__balance -= amount
            self.__transactions.append(f"Withdrew ₹{amount}")
            print(f"₹{amount} withdrawn successfully. New Balance: ₹{self.__balance}")
    def check_balance(self):
        print(f"Account Holder: {self.__holder_name}")
        print(f"Account Number: {self.__acc_no}")
        print(f"Current Balance: ₹{self.__balance}")
    def transaction_summary(self):
        print("\n===== Transaction Summary =====")
        for txn in self.__transactions:
            print(txn)
        print("================================")
def main():
    account = BankAccount(101, "Hitha", 5000)
    account.deposit(2000)
    account.withdraw(3000)
    account.withdraw(5000)
    account.check_balance()
    account.transaction_summary()
if __name__ == "__main__":
    main()
