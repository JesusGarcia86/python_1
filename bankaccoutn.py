class BankAccount:		
    def __init__(self, int_rate, balance):
        self.int_rate = 0.01
        self.balance = 100
   
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"BankAccount: {self.int_rate}, Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance * self.int_rate
        return self
    
maria = BankAccount(0.01, 100)
elina = BankAccount(0.01, 100)

maria.deposit(100).maria.deposit(200).maria.deposit(500).maria.withdrawal(300).maria.yield_interest().maria.display_account_info()

elina.deposit(400).elina.deposite(400).elina.withdrawal(100).elina.withdrawal(50).elina.withdrawal(150).elina.withdrawal(200).elina.yield_interest().elina.display_account_info()