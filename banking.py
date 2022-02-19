class User:
    bank_name = "Franklins Bank Foo"
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

guido = User("gudio", "gueeds@python.org")
monty = User("monty", "soypython.grr")

print(guido.name,"  ", guido.email_address)
print(monty.name)

