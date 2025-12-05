class BankAccount:
    def __init__(self,account_number):
        self.account_number=account_number
        self.balance=0

    def deposit(self,amount):   
        if amount>0:
            self.balance += amount

    def withdraw(self,amount):  
        if 0<amount<=self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account")
    

    def display_balance(self):
        print(f"Bank Account No: {self.account_number}")
        print(f"Balance: PLN {self.balance:.2f}")