#Input()
'''
>> In python, we make use of a function called input() to get the input
   from the user.
The syntax used is :
Var_name = input('string')

>> The input which is taken by input statement will always be in the form
   of string type.
>> To get the required type value, typecasting is required.

>> We cannot take input for list, tuple, set and dictionary with the
   help of single input statement.


'''
#To get input for int
a = int(input('enter the value'))
Print(a)
Print(type(a))
#To get input for float,
a = float(input('enter the value'))
Print(a)
Print(type(a))
#To get input for complex,
a = complex(input('enter the value'))
Print(a)
Print(type(a))
#To get input for bool,
a = bool(input('enter the value'))
Print(a)
Print(type(a))
#########################################################################
         
'''
Eval()
>> It is a built in function python, used to dynamically evaluate
   expression from a string-based or compiled-code-based input.

The syntax used is :
Var_name = eval(input('string'))
'''
###############################################################
#print() statements
'''
>> It is a statement which is used to display the output on the screen.

>> In python we make use of function called print() to display output on
   the screen.
         
Syntax:
Print(any_number_arguments, sep = ' ' , end = '\n')
sep :-
    string inserted between values, default a space.
end :-
    string appended after the last value, default a newline.
         
Ex:
'''
print(10,20,30,40)  #--> 10 20 30 40
print('hello','hai')#-->hello hai
#Whenever we want to change the defalut value for end and separator,
#we can make use of
#Ex :
print('hai', 'hello', 1,2,3,sep = '#',end = '$')
print(10,20,30,end = '*')
print(56,78)
#o/p : hai#hello#1#2#3$10 20 30*56 78
#Programming examples :
#1. WAPTF the sum of 2 int numbers
a = int(input('enter the value : '))
b = int(input('enter the value : '))
print('the sum of number is :',a+b)
#2. WAPTF the cube of given number
num = eval(input('enter the value : '))
print(f'cube of the {num} is : {num**3}')
