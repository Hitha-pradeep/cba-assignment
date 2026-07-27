from datetime import datetime

# ---------------- Transaction ----------------
class Transaction:
    def __init__(self, t_type, amount):
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.type = t_type
        self.amount = amount

    def __str__(self):
        return f"{self.date} | {self.type} | ₹{self.amount}"


# ---------------- Account ----------------
class Account:
    def __init__(self, acc_no, name, balance=0):
        self.__acc_no = acc_no
        self.__name = name
        self.__balance = balance
        self.transactions = []

    def get_balance(self):
        return self.__balance

    def get_acc_no(self):
        return self.__acc_no

    def get_name(self):
        return self.__name

    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(Transaction("Deposit", amount))
        print("₹", amount, "Deposited Successfully")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(Transaction("Withdraw", amount))
            print("₹", amount, "Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    def transfer(self, receiver, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            receiver.deposit(amount)
            self.transactions.append(Transaction("Transfer", amount))
            print("Transfer Successful")
        else:
            print("Insufficient Balance")

    def calculate_interest(self):
        return 0

    def print_statement(self):
        print("\nMini Statement")
        print("--------------------------")
        for t in self.transactions:
            print(t)
        print("Current Balance: ₹", self.__balance)


# ---------------- Savings Account ----------------
class SavingsAccount(Account):
    INTEREST_RATE = 5

    def calculate_interest(self):
        interest = self.get_balance() * SavingsAccount.INTEREST_RATE / 100
        print("Interest = ₹", interest)


# ---------------- Current Account ----------------
class CurrentAccount(Account):
    OVERDRAFT = 5000

    def withdraw(self, amount):
        if amount <= self.get_balance() + CurrentAccount.OVERDRAFT:
            balance = self.get_balance() - amount

            # Accessing private variable using name mangling
            self._Account__balance = balance

            self.transactions.append(Transaction("Withdraw", amount))
            print("Withdrawal Successful")
        else:
            print("Overdraft Limit Exceeded")

    def calculate_interest(self):
        print("Current Account does not earn interest.")


# ---------------- Bank ----------------
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account):
        self.accounts[account.get_acc_no()] = account
        print("Account Created Successfully")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)


# ---------------- Main ----------------
bank = Bank()

# Create Accounts
acc1 = SavingsAccount(101, "Alice", 10000)
acc2 = CurrentAccount(102, "Bob", 5000)

bank.create_account(acc1)
bank.create_account(acc2)

# Deposit
acc1.deposit(2000)

# Withdraw
acc1.withdraw(3000)

# Transfer
acc1.transfer(acc2, 1000)

# Interest
acc1.calculate_interest()
acc2.calculate_interest()

# Current Account Overdraft
acc2.withdraw(9000)

# Mini Statements
acc1.print_statement()
acc2.print_statement()
