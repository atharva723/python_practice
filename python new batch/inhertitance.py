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
        
c1=Bank("atharva",700)
c2=Bank("david",800)


class Savings_acc(Bank):
    interest=0.05
    def __init__(self,name,balance,phno):
        super().__init__(name,balance)      #upadting the init method from parent class(constructor chaining)
        self.phno=phno
    def withdraw(self,amount):
        if amount<500:
            raise ValueError("you withdraw amount of minimum 500 ")
        super().withdraw(amount)                                    #upadting the withdraw method from parent class(method chaining)        

s1=Savings_acc('Atharva',4590,8291632871)


class SalaryACC(Savings_acc):
    interest=0.08
    def deposit(self,amount):
        if amount<10000:
            raise ValueError("AMOUNT should be greater than 10000")
        super().deposit(amount)

e1=SalaryACC("Anuj",50000,778548962)
e=SalaryACC("Ravi",47000,879548962)



#in multiple inheritence parents should not be dependent i.e there should not be common functionalities
class CUSTOMER_data:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transaction=[f"initial balance {self.balance}"]

class Deposit:
    def deposit(self,amount):
        if amount<0:
            raise ValueError("amount should be greater than 0")
        self.balance+=amount
        self.transaction.append(f"the amount of {amount} deposited")


class WITHDRAW:
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient balance")
        self.balance+=amount
        self.transaction.append(f"the amount of {amount} withdrawn")

    
class TRANSFER:
    def transfer(self,rece,amount):
        self.withdraw(amount)
        rece.deposit(amount)
        self.transaction.append(f"the amount of {amount} transfered to {rece.name}")
        rece.transaction.append(f"the amount of {amount} received ")

class MAIN_AC(CUSTOMER_data,Deposit,WITHDRAW,TRANSFER):
    pass

a1=MAIN_AC("ravi",458000)
    
    














