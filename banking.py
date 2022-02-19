class User:
    bank_name = "Dojo Financial Institution"
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"Hello {self.name}, Your current account balance is {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance+=amount
        return self

guido = User ("Guido Cheetos", "Gueeds@Cheese.com")

patrick= User("Patrick Star", "imastar@spongbob.com")

aaron= User("Aaron Carter", "ImInDebt@Massivley.com")

guido.make_deposit(100).make_deposit(400).make_withdrawl(75).display_user_balance()

patrick.make_deposit(85).make_deposit(185).make_withdrawl(30).make_withdrawl(20).display_user_balance()

aaron.make_deposit(25000000).make_withdrawl(16000000).make_withdrawl(14000000).make_withdrawl(6000000).display_user_balance()

patrick.transfer_money(guido, 20)

guido.display_user_balance()
patrick.display_user_balance()
