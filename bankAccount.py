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

class User: 
    def __init__(self, name):
        self.name = name
        self.account = {
            "savings" : BankAccount(.07, 2500),
            "checking": BankAccount(.03, 1200)
        }

    def display_user_balance(self):
        print(f"Member: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"Member: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

frank = User('Franklin')

frank.account['checking'].deposit(1000)
frank.display_user_balance()
