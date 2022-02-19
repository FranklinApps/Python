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

guido = User ("Guido Cheetos", "Gueeds@Cheese.com")
guido.make_deposit(850)
guido.make_withdrawl(317.4)

print(guido.account_balance)

# Hi mom