number = list([1,2])
t_numbers = (1,2)
s_num = {1,2}
d_num = {'a':1,'b':2}

class Point:
    a=1
    b=2
obj=Point()
obj1=Point()

class Point:
    a = 1
    b = 2
    c = 3
    def add():
        return a+b
    
    
ob1= Point()
ob2= Point()
print('before modification class data', Point.a,Point.b,Point.c)
print('before modify obj1 data',ob1.a,ob1.b,ob1.c)
print('before modity obj2 data',ob2.a,ob2.b,ob2.c)
Point.a=11
ob1.x=33
ob2.c=44
print('ofter modifiction')
print(Point.a,Point.b,Point.c)
print(ob1.a,ob1.b,ob1.c)
print(ob2.a,ob2.b,ob2.c)



class School:
    sname='pyspider'
    loc='rajajinagar'
    sub='python'

Amith=School()
Rocky=School()
print(School.sname,School.loc,School.sub)
print(Amith.sname,Amith.loc,Amith.sub)
print(Rocky.sname,Rocky.loc,Rocky.sub)
Amith.phno=9900887766
Amith.addre='Bangalore'
Rocky.sub='python fullstock'

print(School.sname,School.loc,School.sub)
print(Amith.sname,Amith.loc,Amith.sub)
print(Rocky.sname,Rocky.loc,Rocky.sub)

#############################################

class Bank:
    Bname='SBI'
    MBL='Bangalore'
    CEO='Yash'
c=Bank()
c1=Bank()
c1.cname='steve'
c1.balance=1000
c1.phno=9900231144
c2=Bank()
c2.cname='John'
c2.balance=2000
c2.phno=9945786455
c3=Bank()
c3.cname='mark'
c3.balance=3000
c3.phno=8877996655
c4=Bank()
c4.cname='bill'
c4.balance=6000
c4.phno=8899776655



#################################################
#use of __init__ method

class Bank:
    Bname='SBI'
    MBL='Bangalore'
    CEO='Yash'
c=Bank()
c1=Bank()
c2=Bank()
c3=Bank()
def c_details(obj,cname,balance,phno):
    obj.cname=cname #c1.cname='steve'
    obj.balance=balance
    obj.phno=phno
c_details(c1,'steve',1000,9900887766)
c_details(c2,'john',2000,9977880066)
c_details(c3,'bill',6000,8899776655)


#############################################


class Bank:
    Bname='SBI'
    MBL='Bangalore'
    CEO='Yash'
    def c_details(obj,cname,balance,phno):
        obj.cname=cname #c1.cname='steve'
        obj.balance=balance
        obj.phno=phno
c=Bank()
c1=Bank()
c2=Bank()
c3=Bank()

Bank.c_details(c1,'steve',1000,9900887766)
Bank.c_details(c2,'john',2000,9977880066)
Bank.c_details(c3,'bill',6000,8899776655)


#########################################################
class Bank:
    Bname='SBI'
    MBL='Bangalore'
    CEO='Yash'
    def __init__(obj,cname,balance,phno):
        print('__init__ is called')
        obj.cname=cname #c1.cname='steve'
        obj.balance=balance
        obj.phno=phno

c1=Bank('steve',1000,9900887766)
c2=Bank('john',2000,9977880066)
c3=Bank('bill',6000,8899776655)

##Bank.__init__(c1,)
##Bank.__init__(c2,)
##Bank.__init__(c3,)


#####################################
class Bank:
    Bname='SBI'
    MBL='Bangalore'
    CEO='Yash'
    def __init__(self,cname,balance,phno):
        print('__init__ is called')
        self.cname=cname #c1.cname='steve'
        self.balance=balance
        self.phno=phno

c1=Bank('steve',1000,9900887766)
c2=Bank('john',2000,9977880066)
c3=Bank('bill',6000,8899776655)

########################################################
#Types of method/behaviours/functionalities
'''
In class we can store 3 types of methods
1.Object method
2.Class method
3.Static method
1.Object method :-
		>>object method is a method is used to access and modify the members of object.
>> for all the object methods passing self is mandatory to store the address of object.
>>If we are calling an object method by using class then we have to pass the address of object.
>> If we are calling a object method with respect to object then no need to pass the address of object,by default the self will take the respective address of an object

#---------------------------------------------------------------------
2.Class method :-
>> Class method is a method which is used to access and modify the members of class.
>> For all the class methods we have to decorate with “@classmethod”
>> For all the class method passing  “cls” is mandatory to store the address of class.
#---------------------------------------------------------------------

3.Static method :-
>> Static method is a method which is neither belongs to class nor belongs to object but will act as
 supportive method for class and object.
>> To create any static method we have to use a decorator called @staticmethod
>> Since staticmethod is neither belongs to class nor belongs object passing cls or self to
store the address is not required.

'''
class Company:
    cname = 'apple'
    CEO ='steve jobs'
    Loc = 'California'
    def __init__(self,ename,phno,eid,gmail,pay):
        self.ename = ename
        self.phno = phno
        self.eid = eid
        self.gmail = gmail
        self.pay = pay
    def disp(self):
        print(self.ename,self.phno,self.eid,self.gmail,self.pay)
    def new_phno(self,new):
        self.phno = new
    def ch_gmail(self,new_gmail):
        self.gmail = new_gmail
    @classmethod
    def ch_loc(cls,new_loc):
       cls.Loc = new_loc
    @classmethod
    def ch_ceo(cls,New_ceo):
        cls.CEO = New_ceo
    @staticmethod
    def to_print():
        print('it as statict method')
    @staticmethod
    def email():
        return input('enter the new gmail:')
    def email1():
        return input('enter the new gmail:')
    
E1=Company('yash',7788996655,21,'yash@gmail.com',1000)
E2=Company('Rocky',2233445566,22,'rocky@gmail.com',2000)
##print(Company.disp(E1)) # no error
##print(Company.disp(Company))#raise an error becouse it object method
##print(Company.ch_loc('Newyork') #no error
##print(Company.ch_loc(E1,'Newyork') #it raise error becouse it is class method
print(Company.email())
print(E1.email())

##print(Company.email1()) #RAISE ERROR
##print(E1.email1())#Raise error becouse it is not staticmethod

#####################################################################################################

'''

INCAPSULATION /ACCESS SPECIFIERS :-
ACCESS SPECIFIERS are the members of the class which will tell the user whether
they can access it outside
-the class or not.
Access specifiers are got classified into 3 types.
1 public
2 protected
3 private
1.Public access specifiers:-
>> These are the members of the class ,it is possible to access all these members
outside the class. or
>> Public access spefiers are the one ,which will allow the user to access them
outside the class.
>>The members which are creating inside the class generally will be considered as
public access specifiers.
>> example :-
'''
class Sam:
    a = 10
    b = 20
    def __init__(self,c,d):
        self.c = c
        self.d =d
    def disp(self):
        print(self.c,self.d)
    @classmethod
    def display(cls):
        print(cls.a,cls.b)
    @staticmethod
    def msg():
        print('hii')
ob1 = Sam(100,200)
ob2 = Sam(300,400)
print(Sam.a)
ob1.disp()
Sam.display()
Sam.msg()

##################################
'''
2.Protected access specifiers :-
>> These are members ,which should give the protection to the data store inside the
class
but in python protected members will not give any security (it will act like
public members)
>> because of the above reason protected members are not in use.
>> To create any protected members _variable or _methodname
>>example
'''
class Sam:
    _a = 10
    _b = 20
    def __init__(self,c,d):
        self._c = c
        self._d =d
    def _disp(self):
        print(self.c,self.d)
    @classmethod
    def _display(cls):
        print(cls.a,cls.b)
    @staticmethod
    def _msg():
        print('hii')
ob1 = Sam(100,200)
ob2 = Sam(300,400)
print(Sam._a)
ob1._disp()
Sam._display()
Sam._msg()
######################################################################
'''
>>
3.Private access specifiers :-
>> these are the members of the class ,which will not allow the to access them
outside the class.
>> To create private members we have to use __variable or __methodname
>>example
'''
class Sam:
    __a = 10
    __b = 20
    def __init__(self,c,d):
        self._c = c
        self._d =d
    def _disp(self):
        print(self.c,self.d)
    @classmethod
    def __display(cls):
        print(cls.a,cls.b)
    @staticmethod
    def _msg():
        print('hii')
ob1 = Sam(100,200)
ob2 = Sam(300,400)



########################################################################################################





    








