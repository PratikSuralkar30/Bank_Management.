class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposite(self, amount):
            self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
                self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: ₹{}".format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s Current Account : Balance ₹{}".format(self.name, self.balance)

class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Saving Account : Balance ₹{}".format(self.name, self.balance)



'''
OUTPUT

Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: F:\Diploma courses by IITB\Python\Python Programming\python code\P11_Bank.py
P = Current("Pratik", 500)
P.deposite(300)
P.statement()
Account Balance: £800
P.withdraw(1000)
P.statement()
Account Balance: £-200
P.withdraw(800)
P.statement()
Account Balance: £-1000
P.withdraw(1)
Sorry, not enough funds!
print(P)
Pratik's Current Account : Balance £-1000
T = Saving("Tom", 300)
print(T)
Tom's Saving Account : Balance £300
T.withdraw(300)
T.statement()
Account Balance: £0
T.withdraw(1)
Sorry, not enough funds!

'''
