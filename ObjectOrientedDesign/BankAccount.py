'''
Write a small class to emulate a bank account

1. A Bank account should have ac_number, ac_name, ac_balance, ac_type
2. Should take deposits and withdrawl
3. Should provide interest
'''

class BankAccount:

    # Defining class attributes
    default_interest_rate = 0.07

    def __init__(self, ac_number:int, ac_name:str, ac_type:str, ac_balance:float=0.0):
        self.ac_number = ac_number
        self.ac_name = ac_name
        self.ac_balance = ac_balance
        self.ac_type = ac_type

    def withdrawl(self, amount:float):
        if self.ac_balance < amount:
            return f'Withdrawl amount of {amount} is higher that the total account balance of {self.ac_balance}'
        else:
            self.ac_balance -= amount
    
    def deposit(self, amount:float):
        self.ac_balance += amount

if __name__ == "__main__":
    # Created an object of class BankAccount
    acc = BankAccount(1111, "Account1", "Savings")
    print(acc.ac_balance)
    print(acc.withdrawl(100))
    print(acc.ac_balance)
    acc.deposit(1000)
    print(acc.ac_balance)
    print(acc.withdrawl(100))
    print(acc.ac_balance)


