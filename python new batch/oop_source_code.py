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
