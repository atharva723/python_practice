class ATM:
    def __init__(self,name,acc_no,balance,bank_pin):
        self.bank_pin=bank_pin
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
    def withdraw(self,pin):
        while True:
            if self.bank_pin!=pin:
                raise ValueError ("Incorrect pin, Try again")
            else:
                self.balance-=amount
                break
    def deposit(self,amount,pin):
        while True:
            if self.bank_pin!=pin:
                raise ValueError ("Incorrect pin, Try again")
            else:
                self.balance+=amount
                break
    def reset_pin(self,acc_no)      

c1=ATM("Atharva",2000,123)
c2=ATM("david",37374,233)




