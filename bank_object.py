class bank:
    def __init__(self, accountnum, username, name, password, balance):
        self.accountnum = accountnum
        self.username = username
        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return "AMOUNT ADDED SUCESSFULLY"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return "AMOUNT WITHDRAW SUCESSFULLY"
        else:
            return "AMOUNT IS GREATER THAN BALANCE AMOUNT"
    
    def check(self):
        return str(self.balance)
