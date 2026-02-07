
##polymorphism
##
##'''it is a process of making a single operator to work an two different operations or
##making a method to work an two different functionalities'''
##
##
##polymorphism can be explained by useing following process
##1. method overloading
##2.operator overloading
##
##1.method overloading :-
##>> Method overloading a phenomenon of making the a same method or function to work an two or
##   more different functionalities.
##   
def add(a=0,b=1,c=0):  # method overloading
    return a+b+c
print(add(1))
print(add(1,2))
print(add(1,3,4))
print(add())

class Point:
    def __init__(self,a=0,b=0):
        self.a = a
        self.b = b
ob1 = Point(1,2)
ob2 = Point(4)
ob3 = Point()
##class BankAccount :  
##    INTEREST_RATE = 0.04
##    def __init__(self, name, balance):
##        self.name = name
##        self.balance = balance
##        self.transactions = [ ]
##        self.transactions.append(f"Inital amount deposited {balance}")
##
##    def deposit(self, amount):
##        if amount < 0:
##            raise ValueError("amount should be greater than zero")
##        self.balance = self.balance + amount
##        self.transactions.append(f"Amount deposited {amount}")
##
##    def withdraw(self, amount):
##        if amount > self.balance:
##            raise ValueError("insufficient funds")
##        self.balance = self.balance - amount
##        self.transactions.append(f"Amount withdrawn {amount}")
##
##    def statement(self):
##        for transaction in self.transactions:
##            print(transaction)
##        print("*"*30)
##        print(f"total available balance {self.balance}")
##
##    def roi(self):
##        interest_amount = self.balance * self.__class__.INTEREST_RATE
##        self.balance = self.balance + interest_amount
##        self.transactions.append(f"Interest amount credited {interest_amount}")
##
##class SavingsBankAccount(BankAccount):
##    INTEREST_RATE = 0.035
##    def deposit(self,amount=2000): #over-loaded to child class method
##        if amount<1000:
##            raise ValueError(f' min deposite should be more than 1000')
##        super().deposit(amount)
##        
##        
##sba =SavingsBankAccount('steve',1000)  
##sba.deposit()
##############################################################
##
####method over-riding
#'''Method overriding is when we create two different functions with the same name in 
single file
#   then the address of previous function will get overided by the address of next 
function,so that we can't access the previous function'''
##def add(a,b):       
##    return a+b
##
##def add(a,b,c):
##    return a+b
##


##class BankAccount :  
##    INTEREST_RATE = 0.04
##    def __init__(self, name, balance):
##        self.name = name
##        self.balance = balance
##        self.transactions = [ ]
##        self.transactions.append(f"Inital amount deposited {balance}")
##
##    def deposit(self, amount):
##        if amount < 0:
##            raise ValueError("amount should be greater than zero")
##        self.balance = self.balance + amount
##        self.transactions.append(f"Amount deposited {amount}")
##
##    def withdraw(self, amount):
##        if amount > self.balance:
##            raise ValueError("insufficient funds")
##        self.balance = self.balance - amount
##        self.transactions.append(f"Amount withdrawn {amount}")
##
##    def statement(self):
##        for transaction in self.transactions:
##            print(transaction)
##        print("*"*30)
##        print(f"total available balance {self.balance}")
##
##    def roi(self):
##        interest_amount = self.balance * self.__class__.INTEREST_RATE
##        self.balance = self.balance + interest_amount
##        self.transactions.append(f"Interest amount credited {interest_amount}")
##
##class SavingsBankAccount(BankAccount):
##    INTEREST_RATE = 0.035
##    def withdraw(self,amount):  #over-riding an parent class methed in child class completely
##        raise ValueError(f"you can't withdraw the amount from this account")
##       
##        
##sba =SavingsBankAccount('steve',1000)  
###sba.withdraw(1000)
##''' Overriding vs Overloading
##1. Overriding is a concept in which if objects are with same name then
##latest one will be retained
##2. Overloading is a concept in which if the functions/methods with
##same name have different arguments, each can be called with respect to their arguments.'''
##
##
##
##############################################################
##
####operator overloading :-
##'''>> All the operator will support for the objectes of inbuilt class or inbuilt data type 
# but some of the
##   operator will support the object of user defined data types or user defined class.
##>> operator overloadingit is a phenomenon of making the operators to work an the object of
#  user defined
##   datatype by invoking the respective magic method.
## '''
##class Point:
##    def __init__(self,a):
##        self.a = a
##    def __add__(self,other):
##        print('add method is called')
##        return self.a+other.a
##    def __sub__(self,other):
##        return self.a-other.a
##    def __mul__(self,other):
##        return self.a*other.a
##    
##c1 = Point(4)
##c2 = Point(2)
##c3 = Point(8)
##
##############################################################
##
####Absraction
##'''
##>>it is a phenomenon of hiding the features or functionalities from  the user
##>> To understand obstraction we should know the following keywords
##1.Abstract method
##2.Abstract class
##3.concrete class
##'''
###--------------------------------------------------------------------------------------
##
###1.Abstract method:-
###>>it is a method, which should have function declaraction but not the function defination
##class Cname:
##    def fname(args):   #---->function declaraction is there
##        pass           #------> no defiction
###--------------------------------------------------------------------------------------
###2.Abstract class:-
###>> It is a class, which should consists of atleast one abstract method in it.
###>> It is not possible to create obeject for abstract class


from abc import ABC,abstractmethod

class Sam(ABC):
    @abstractmethod
    def msg():
        pass
    @abstractmethod
    def demo():
        pass
s= Sam()
    
###--------------------------------------------------------------------------------------
###3.concrete class
###>> it the class does not consist any abstract method then we can call it is concrete class
##class Sam:
##    def msg():
##        pass
##    def demo():
##        pass
###--------------------------------------------------------------------------------------
###abstraction behavoir
##class SukanyaSamruthdiAccount(BankAccount):
##    INTEREST_RATE = 0.08
##
##    
##sba =SavingsBankAccount('steve',1000)  
###SukanyaSamruthdiAccount class object (sba) don't about features or functionalities (code implimentation)
###in BankAccount class
###--------------------------------------------------------------------------------------
##
