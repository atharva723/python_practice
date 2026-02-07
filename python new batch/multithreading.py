'''                    math module
It is an inbuilt module which is consist of different mathematical functions.
in it.,    factorial(number),sqrt(num),floor(num),pi….'''

from math import sqrt,factorial,pi,floor

##print(sqrt(3))# sqrt it function used to get the square root  of any number'
##print(factorial(3)) ##  factorialit function used to get the  factorial of any number'
##
##print(floor(3)) #it is a function used to get the floor division number'
##print(pi) #it built in variable in math module of pi value'


#Random module:
'''It is an inbuilt module which is used to generate the random numbers
To extract random number etc.
Random(),randint(),choice(),shuffle().'''

from random import random,randint,choice,shuffle

print(random()) #it is function it well generate random number between 0 to 1.
print(randint(1,20)) #it is function it well generate random number between specified limit.
data=[19,8,1998,'Aug',20,2,1991]
print(choice(data)) #it is function which will choice value from given collection
                    #randomlly
data=[19,8,1998,'Aug',20,2,1991]

shuffle(data) #it is function which shuffle the values in given collection randomlly 

print(data)











#----------------------------------------------
#multi threading
'''
Thread is smallest part of the program.
Multi threading is a phenomenon of executing two or more tasks parallelly to save the execution time.
Multithreading can be done only if tasks are independent to each other 
'''
import threading
from time import sleep
def add(a,b):
    sleep(1)
    print(a+b)
def sub(a,b):
    sleep(3)
    print(a-b)

def get():
    a=int(input('Enter :'))
    b=int(input('Enter :'))
    return a,b
def sam():
    m,n=get()
    print(m,n)
    
import threading
import time

# Function to be run by each thread
def print_numbers(thread_name, delay):
    for i in range(5):
        time.sleep(delay)
        print(f"{thread_name} is printing number {i}")

# Creating threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 1))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 2))

# Starting threads
#thread1.start()
#thread2.start()

# Joining threads to ensure they complete before the main thread exits
#thread1.join()
#thread2.join()

print("Both threads have finished execution.")

from threading import *
from time import sleep

##
##
##def add():
##    sleep(2)
##    print(2+4)
##
##def mul():
##    sleep(1)
##    print(5*4)
##
##
##t1=Thread(target=add)
##t2=Thread(target=mul)
##t1.start()
##t2.start()






















##class User(Thread):
##    names=['steve','bill','tim','yash']
##    def details(self):
##        for i in range(4):
##            sleep(2)
##            print(f'user_name : {User.names[i]}')
##
##
##class cart(Thread):
##    items=['iphone','imac','iwatch','ipad']
##    def product(self):
##        for i in range(4):
##            sleep(1)
##            print(f'product : {cart.items[i]}')
##
##u=User()
##c=cart()
##u.start()
##c.start()
##u.join()
##c.join()









##names=['steve','bill','tim','yash']
##items=['iphone','imac','iwatch','ipad']
##
##def loop(collection,sec):
##    for item in collection:
##        sleep(sec)
##        print(item,end='-')
##
##
##thread1 = Thread(target=loop, args=(names,1))
##thread2 = Thread(target=loop, args=(items,1))
##
### Starting threads
##thread1.start()
##thread2.start()
##
### Joining threads to ensure they complete before the main thread exits
##thread1.join()
##thread2.join()






from threading import *
from time import sleep


def even_numbers(n):
    n=int(n)
    while True:
        print(n)
        sleep(1)
        n+=1

def odd_numbers(n):
    n=int(n)
    while True:
        print(n)
        sleep(1)
        n+=1




##task1=Thread(target=even_numbers,args=('1'))
##task2=Thread(target=odd_numbers,args=('2'))
##task1.start()
##task2.start()
##task1.join()
##task2.join()
def project_work():
    sleep(1)
    print('project work is done')

def daily_report():
    sleep(1)
    print('daily report sent')

def Hr_report():
    sleep(1)
    print('Hr report sent')



t1=Thread(target=project_work)
t2=Thread(target=daily_report)
t3=Thread(target=Hr_report)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print('my all works are completed')







