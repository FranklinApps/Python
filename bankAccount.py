class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.intrest = int_rate 
        self.account_balance= balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance > 0: 
            self.account_balance-= amount
            return self
        else:
            print("insufficient funds: -$5 ")
            self.account_balance -= 5
            return self

    def display_account_info(self):
        print("Your account balance is: %s" %self.account_balance)
        return self

    def yield_intrest(self):
        if self.account_balance > 0:
            self.account_balance += (self.intrest * self.account_balance)
        return self 

    @classmethod
    def display_all_accounts(cls):
        for account in cls.accounts:
            account.display_all_accounts()

savings = BankAccount(.04, 18000)
checking = BankAccount(.01, 6000)

savings.deposit(40).deposit(460).deposit(250).withdraw(275).yield_intrest().display_account_info()
checking.deposit(30).deposit(420).deposit(69).withdraw(1275).yield_intrest().display_account_info()

BankAccount.display_all_accounts()
