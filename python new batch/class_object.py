class Point:
    a=1
    b=2
    def add(p,q):
        return p+q
ob1=Point()
ob2=Point()
print(ob1.__dict__)
print(ob2.__dict__)
ob1.a=18
ob1.u=99
print(ob1.__dict__)
