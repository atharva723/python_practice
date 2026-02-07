'''
for loop :-
>>for is a looping statement,which is used to execute same set of instruction
 repeatitively again and again.

>> in for loop initiolization and updation of looing variable is automated.

>> It is possible to get the values one by one directly using for loop.

synatax :
    for value in collection:
        statement block
'''










#--------------------range()-------------------------------------------
'''
range():-range is a function which is used to create the sequance of numbers 
b/w the specified limits.
range() is not having proper structur to display the values ,
because of this resion type casting is required

syntax:
    range(staring_value,ending_value,updation)


>>in range starting value is included and ending 
value is exclueded and updation by default 1

>>if represent only one value in range(101) ,that will 
take it as end value, by default srting value 0 . 
'''
#WAP TO print list of numbers from 1 to 100

print(list(range(1,101,1)))

print(tuple(range(1,101,1)))

print(set(range(1,101,1)))



###########################################################################3

#1.WAPT print each value in given collection useing while loop.
data = eval(input('enter the collection :'))
i = 0
while i<len(data):
    print(data[i])
    i+=1

#########################################################################3
#1.WAPT print each value in given collection useing for loop.
data = eval(input('enter the collection :'))
for i in data:
    print(i)

#########################################################################3
#2.WAPs to print all data elements from any collection type

for char in 'word':
    print(char)


for element in [10,20,30,40]:
    print(element)


for value in (2,3,4,5,6,5,7,7,8,9,10):
    print(value)

for value in {8,4,6,9,3,2}:
    print(value)

for key in {'a':1,'b':2,'c':3}:
    print(key)

for item in {'a':1,'b':2,'c':3}.items():
    print(item)

    
for value in {'a':1,'b':2,'c':3}.values():
    print(value)


#########################################################################3

##3. WAP to extract all uppercase vowel present inside given sting.

st = input('enter the string') # YAlleShA ROcKY'
out = ''
for char in st:
    if char in 'AEIOU':  
        out = out+char
print(out)

############################################################################################
#4. WAP TO FIND LENGTH OF GIVEN COLLECTION WITHOUT USING LEN FUNCTION

S = eval(input('enter the collection'))

count = 0
for value in S:
    count = count+1
print(count)

##################################################################################################
#5. WAP to extract all uppercase and lowecase and digit and special symbols,seperately from give string
st = 'YAlleSH@19$'
us,ls,n,ss = '','','',''

for char in st:
    if 'A'<=char<='Z':
        us+=char
    elif 'a'<=char<='z':
        ls+=char
    elif '0'<=char<='9':
        n+=char
    else:
        ss+=char
print(us,ls,n,ss)

##################################################################################################
#6.WAP TO COUNT THE SPECIFIED CHARACTER FROM THE GIVEN STRING.

greet = input('enter the string')
char = input('enter the char')
c = 0
for value in greet:
    if value == char:
        c+=1
print(c)

##################################################################################################
#7.WAP TO PRINT NUMBERS FROM 1 TO 10 using while.
i=1
while i<=10:
    print(i)
    i+=1
#7.WAP TO PRINT NUMBERS FROM 1 TO 10 using  for loop.
for number in range(2,101,2):
    print(number)
##################################################################################################
#8.WAP to find the factorial of a given no.
n = int(input('enter the number'))   # 4 ,4*3*2*1=24,5 = #5*4*3*2*1 = 120
out = 1  # 1,2,6,24
for i in range(1,n+1):               #n=4 range(1,5)# [1,2,3,4]
    out = out*i
print(out)

##################################################################################################
    
#9.WAP to print the devices of given number.  # 6 =1,2,3,6

n1 = int(input('enter number')) #6===>

for i in range(1,n1):
    if n1%i==0:               #6%1==0,6%2==0(T),6%3==0(T),6%4==0(f),6%5==0(f),6%6==0(t)
        print(i)

##################################################################################################

#10.WAP to print sum of the devices of given number excluding that number and also,
#10.WAP to check wheather given numbers is perfect number or not.
n = int(input('enter number'))                     #6===>1,2,3 ==1+2+3 =6
sum = 0
for i in range(1,n):
    if n%i==0:                             #6%1==0,6%2==0(T),6%3==0(T),6%4==0(f),6%5==0(f),6%6==0(t)
        sum = sum+i
print(sum)

if n==sum:
    print('that is perfect numbers')
else:
    print('it is not a perfect number')


'''perfect number =     #6===>1,2,3 ==1+2+3 =6   
positeve integer number that is equal to the sum of it's positive divisors excluid the number itself'''
#######################################################################################################

#11.WPA to find the sum of ASCII value of all
#Uppercase charectors inside string'

string = input('enter the string') # 'GREET to SOme ONE N0w 234'
sum = 0
for char in string:
    if 'A'<=char<='Z':
        sum+=ord(char)
print(sum)

#######################################################################################################

#12.WAP TO print qube of all the even number which are divisible by 4, between range m to n.

m = int(input('enter the string number :'))
n = int(input('enter the ending numbre :'))
for number in range(m,n+1):
    if number%2==0 and number%4==0:
        print(number,number**3)

#######################################################################################################

#13.WAP TO PRINT MULTIPLICCATION TABLE FOR ANY NUMBER

n = int(input('enter the number'))
for i in range(1,11):
    print(f"{n}X{i} = {n*i}")

#######################################################################################################
#14.WAP to print sum of n nutural numbers :

n = int(input('enter the number'))
sum = 0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#######################################################################################################

#15.WAP to get sum of all integer number present inside the list

list1 = eval(input('enter the collection'))
result = 0
for item in list1:
    if type(item)==int:
        result+=item
print(result)

#######################################################################################################

#16.WAP to reverse the string with out using built in functions

st = 'apple'
rev = '' 
for char in st:
    rev= char+rev
print(rev)


'''
tracing
1.char = 'a',    'a' in 'apple'  (T)====> rev = 'a'+' ' ===>  'a'
2.char = 'p',    'p' in 'apple'  (T)====> rev = 'p'+'a' ===>  'pa'
3.char = 'p',    'p' in 'apple'  (T)====> rev = 'p'+'pa'===>  'ppa'
4.char = 'l',    'l' in 'apple'  (T)====> rev = 'l'+'ppa'===> 'lppa'
5.char = 'e',    'e' in 'apple'  (T)====> rev = 'e'+'lppa'===>'elppa'

'''
#######################################################################################################


#17.WAP to get following output,
##input = 'hello'
#output = {0:'h',1:'e',2:'l',3:'l',4:'o'}

ip = 'hello'
out = {}

for i in range(0,len(ip)):
    out[i] = ip[i]
    print(out)
print(out)


#######################################################################################################

#18.WAP to get following output,
#input = ['hai','hello','how','are','you']
#output = {'hai':3,'hello':5,'how':3,'are':3,'you':3}

a = ['hai','hello','how','are','you']
out = {}
for item in a:
    out[item] = len(item)
    print(out)

for num in range(65,91):
    break
    print(char(65))
print('loop is breaked')


# -----------------------------------------INTERMEDIATE TEMINATION IN LOOP---------------------------#
'''>>When ever we want to terminate the loop in between ,we should make use of the following keywords.
>>1.break
>>2.continue
>>3.pass     '''

###################################################################################    
'''
1.break :- It is a keyword which is used to terminate the loop in between
>>As soon as control see a keyword called break, it will come out from the loop
  and it will not go for same loop again.
>> break can be used for both while loop and for loop.
>> we can have break keyword without writting any condition but it is of no use.
'''


###################################################################################    

#1.WAP only first uppercase charector

###################################################################################    

#2.WAP TO print smallest diviser of given number other than 1

    


###################################################################################    

#3 WAP to print the initial index of a given charactor present inside the given string.
st = 'hello'
char = 'l'


###################################################################################    


#2.continue:-
""">> continue is a keyaword which is used to skip the current execution and
   to make the control to go the next iteration.
>> 'continue can be use without having any condition but we will not got any output from that'

>> 'break and continue can be used in both while and for loop'
"""
###################################################################################    
#1.WAP to print numbers from 1 to 11 by skiping number 6 and 9


###################################################################################    

#2.WAP to extract all even numbers between the range of 1 to 50 by using continue,


###################################################################################    

#3.WAP to extract all the data items present at odd index in a given list.
a = [1,2,3,4,5,8,'hello','haii']

        
###################################################################################    

'''
pass :-
        >> pass is a keyaword which is used to keep any empty statement block as valied block and
           display the empty statement without displaying the error.
        >> pass can be used in conditional statements,looping statements and fuctions and class.
'''
if 10<20:
    pass
print('hai')


for i in 'apple':
    pass
print('above there is a empty statement')
