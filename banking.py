class User:
    bank_name = "Dojo Financial Institution"
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"Hello {self.name}, Your current account balance is {self.account_balance}")


guido = User ("Guido Cheetos", "Gueeds@Cheese.com")

patrick= User("Patrick Star", "imastar@spongbob.com")

aaron= User("Aaron Carter", "ImInDebt@Massivley.com")

guido.make_deposit(100)
guido.make_deposit(400)
guido.make_withdrawl(75)
guido.display_user_balance()

patrick.make_deposit(85)
patrick.make_deposit(185)
patrick.make_withdrawl(30)
patrick.make_withdrawl(20)
patrick.display_user_balance()

aaron.make_deposit(25000000)
aaron.make_withdrawl(16000000)
aaron.make_withdrawl(14000000)
aaron.make_withdrawl(6000000)
aaron.display_user_balance()
