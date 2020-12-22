class BankAccount:		
    def __init__(self, int_rate, balance):
        self.int_rate = 0.01
        self.balance = 100

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate=0.02, balance=0), BankAccount(int_rate=0.02, balance=100)]

    def make_deposit(self, amount, idx):	
    	self.account[idx].balance += amount

    def make_withdrawal(self, amount, idx):
        self.account[idx].balance -= amount

    def display_user_balance(self, idx):
        print(f"User: {self.name}, Balance: ${self.account[idx].balance}")

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
sofia = User("Sofia Kenin", "skenin@python.com")
elina = User("Elina Svitolina", "esvitolina@python.com")
maria = User("Maria Sharapova", "msharapova@python.com")

guido.make_deposit(100, 0)
guido.make_withdrawal(50, 1)
guido.display_user_balance(1)