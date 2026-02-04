###even number
##def even(a,b):
##    li=[]
##    for i in range(a,b+1):
##        if i%2==0:
##            li.append(i)
##    return li
####    return [i for i in range(a,b+1) if i%2==0]
##print(even(1,10))
###len
##def length(a):
##    count=0
##    for i in a:
##        count+=1
##    return count
###to clarify given list is homogeneous or hetero
##def abc(a):
##    a=list()
##    for i in range(a):
##        
##        if type(a[0])!=type(a[i]):
##            return "hetero"
##     return "homo"

#implement to check given char is upper case or not without using any method
def upper(a):
    if "z"<=a>='a':
        return "upper"
    return "lower"
#count
def rec(b,a):
    
    count=0
    for i in a:
        if i==b:
            count+=1
    return count
#wap to check number is prefect number or not
def perf(a):
    l=[]
    for i in range(1,a):
         if a%2==0:
             l.append(i)
    return sum(l)==sum(range(1,a))
#prime number
def prime(a):
    if a%2!=0 and a%3!=0:
        return "prime"
#armstrong
def arm(a):
    num=str(a)
    l=[]
    for i in num:
        l.append(int(i)**len(num))
    return sum(l)==a

a=10
print(a)
a=a+1
print(a)
def out():
    global a
    a=a+1
    print(a)
out()
print(a)


#sum of minimum of three number and max 5
def s(a,b,c,d=0,e=0):
    return a+b+c+d+e
#prod of minimum 5 max 7
def s(a,b,c,d,e,f=1,g=1):
    return a*b*c*d*e*f*g

#wap to get numbers 1to 20 without any loop
A,*num=range(0,21)

def numb(*args):
    print(args)

from time import sleep
def countup(i=1):
    if i<=20: #recursion termination condition
        sleep(0.5)
        print(i)
        i+=1
        countup(i)
def rev(i=10):
    if i>=1: #recursion termination condition
        if i%2==0:
            print(i)
        i-=1
        rev(i)

#wap to extract only str of value from given list
data=['apple',12,"hello",3.2,True,'bye']
def e(i=0,l=[]):
    if i<len(data):
        if type(data[i])==str:
            l.append(data[i])
        i+=1
        return e(i,l)
    


#factorial
def fact(a):
    if a<=1:
        return 1
    return a*fact(a-1)
    
#
##def fact(a,i=a):
##    if i>=1:
##        i-=1
##        a=a*i
##        fact(a,i)
##    if i<=1:
##        return a

#wap to get names and its length pair in dict
name=['apple','google','TCS',"microsoft"]
def pair(n,d=dict(),i=0):
    if i>=len(n):
        return d
    if i<len(n):
        d[n[i]]=len(n[i])
    i+=1
    return pair(n,d,i)
    
