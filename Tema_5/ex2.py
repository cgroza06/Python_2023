class Account:
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def interest_calculation(self):
        pass

class CheckingAccount(Account):
    def __init__(self, account_number, balance, fee):
        super().__init__(account_number, balance)
        self.fee = fee

    def deduct_fee(self):
        self.balance -= self.fee

    def interest_calculation(self):
        self.balance += self.balance * 0.01

class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.02

    def add_interest(self):
        self.balance += self.balance * self.interest_rate


checking_account = CheckingAccount(123, 500, 5)
savings_account = SavingsAccount(456, 1000)

checking_account.deposit(100)
checking_account.deduct_fee()
checking_account.interest_calculation()
print(checking_account.balance)

savings_account.deposit(100)
savings_account.add_interest()
print(savings_account.balance)

