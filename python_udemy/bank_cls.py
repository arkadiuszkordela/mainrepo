class Bank:
    def __init__(self, account_number, owner_name, balance = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} has been deposited to the account.')
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{amount} has been withdrawn from the account.')
        else:
            print('Insufficient balance.')
    
    def get_balance(self):
        print(f'Account balance: {self.balance}')