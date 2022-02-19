class User:
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

User()
guido = User()
monty = User()

print(guido.name)
print(monty.name)

guido.name = "Guido"
print(guido.name)

monty.name = "Monty"
print(monty.name)

