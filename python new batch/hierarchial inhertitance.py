class Bank:
    interest=0.04
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transaction=[f"initial balance {self.balance}"]
    def deposit(self,amount):
        if amount<0:
            raise ValueError("amount should be greater than 0")
        self.balance+=amount
        self.transaction.append(f"the amount of {amount} deposited")
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient balance")
        self.balance+=amount
        self.transaction.append(f"the amount of {amount} withdrawn")

        
    def transfer(self,rece,amount):
        self.withdraw(amount)
        rece.deposit(amount)
        self.transaction.append(f"the amount of {amount} transfered to {rece.name}")
        rece.transaction.append(f"the amount of {amount} received ")

    def roi(self):
        interest_amount=self.balance*Bank.interest
        self.deposit(interest_amount)
        self.transaction.append(f"the interest amount of {amount} deposited ")
        
    def statement(self):
        print("#"*40)
        for i in self.transaction:
            print(i)
        print("#"*40)
        print(f"total balance : {self.balance}")
        print("#"*40)

class SAVINGS(Bank):
    pass
class SALARY(Bank):
    interest=0.06
class SENIOR(Bank):
    interest=0.08
