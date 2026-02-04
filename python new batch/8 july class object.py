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
        rece.transaction.append(f"the amount of {amount} deposited ")

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
        
c1=Bank("atharva",700)
c2=Bank("david",800)
c1.deposit(4500)
c2.deposit(4855)
c2.withdraw(550)
c1.transfer(c2,250)
c2.withdraw(705)
c2.deposit(450)
c2.transfer(c1,230)
