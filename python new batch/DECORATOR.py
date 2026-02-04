#log message
##def out(func):
##    def wrap(*args,**kwargs):
##        print("LOG MESSAGE:_______")
##        return func(*args,**kwargs)
##    return wrap
##
##@out
##def add(a,b):
##    return a+b

#implement if callback function is str list or tuple it should reverse the output or keep it as it is


def rev(func):
    def wrap(*args,**kwargs):
        if type(func(*args,**kwargs))==str or type(func(*args,**kwargs))==list() or type(func(*args,**kwargs))==tuple() :
            return func(*args,**kwargs)[::-1]
        return func(*args,**kwargs)
    return wrap
@rev
def greet():
    return "HEllO World"


#to convert positive output if there is a negative output any callable
def pos(func):
    def wrap(*args,**kwargs):
        if func(*args,**kwargs)<0:
            result=func(*args,**kwargs)*-1
            return result
        return func(*args,**kwargs)
    return wrap

" ABS: it is a built in function to convert any negative numbers to positive"

def pos(func):
    def wrap(*args,**kwargs):
        return abs(func(*args,**kwargs))
    return wrap
@pos
def add(a,b):
    return a+b
@pos
def mul(a,b):
    return a*b



###
def ke(func):
    def wrap(*args,**kwargs):
        if len(kwargs)==0:
            return "keyword argument not allowed"
        return func(*args,**kwargs)
    return wrap

def ke(func):
    def wrap(*args,**kwargs):
        if not(kwargs):
            return func(*args,**kwargs)
        return "keyword argument not allowed"
    return wrap

@ke
def add(a,b):
    return a+b


#to return time taken for execution of each function

from time import sleep,time

def ex(func):
    
    def wrap(*args,**kwargs):
        start=time()
        result=func(*args,**kwargs)
        stop=time()
        print(f"execution time of function is {stop-start}")
        return result
    return wrap


@ex
def greet():
    sleep(2)
    print("hello world")
    return "good moring"
@ex
def greets(a):
    sleep(1)
    print("hello world")
    return f"hi {a}"

@ex
def mul(a,b,c):
    return a*b*c










