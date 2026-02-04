











#------------------------------------------------------------------------------------------------------

#1.Write a program to print list of numbers between the range 1 to 20.
#without using comprehension.
numbers = []
for number in range(1,21):
    numbers.append(number)
print(numbers)

#with using comprehension.
_numbers = [number for number in range(1,21)]
print(_numbers)
#-----------
#single line
print([number for number in range(1,21)])

#############################################################################################
#2.WAPTP list of charactor in given string,  greet = 'Hello World'
#without using comprehension.
greet = 'Hello World'
letters = []
for char in greet:
    letters.append(char)
print(letters)
#with using comprehension.
print([char for char in greet])

#############################################################################################

#3.WAPTP list of square numbers,which are present given list,numbers = [1,2,3,4,5]
#without using comprehension.
numbers = [1,2,3,4,5]
square_numbers = []
for number in numbers:
    square_numbers.append(number**2)
print(square_numbers)

#with using comprehension.
print([number**2 for number in numbers])

#############################################################################################
#4.# Building a list of first_name and list of last_name from full_names
##    full_names = ["steve jobs", "bill gates", "john doe", "tim cook"]
full_names = ["steve jobs", "bill gates", "john doe", "tim cook"]
# extracting first_name and last_name using list comprehension
first_names = [ name.split()[0]   for name in full_names ]
last_names = [ name.split()[-1]   for name in full_names ]

#############################################################################################
#list comprehension with if condition.
#Variable = [expresion for value in collection if condition]
#5.list of even numbers between range of 1 to 20
#without using comprehension.
even = []
for number in range(1,21):
    if number%2==0:
        even.append(number)
print(even)

#with using comprehension.
_even = [number for number in range(1,21)if number%2==0]

print(_even)

#############################################################################################
#6.WAPTP a list of polindromes from given list.
#names =['steve','eve','john','anna','stella','bob']
#without using comprehension.
names =['steve','eve','john','anna','stella','bob']
polindromes = []
for name in names:
    if name==name[::-1]:
        polindromes.append(name)
print(polindromes)
#with using comprehension.

_polindromes = [name for name in names if name==name[::-1]]
print(_polindromes)

#############################################################################################
#7.Filtering out those names which are less than 6 characters
#names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
short_names = [name for name in names if len(name) < 6]
print(short_names)

#############################################################################################
#8. Filtering all the languages which starts with 'p'
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
p_languages = [language for language in languages if language.lower().startswith('p')]
# Alternate Solution
p_languages = [language for language in languages if language.lower()[0] == 'p']

#############################################################################################
#9. Build a list with only even with even length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
even_string = [name for name in names if len(name) % 2 == 0]

############################################################

# Using "else" in Comprehension
#Variable = [TSB if condition else FSB for item in data]
#10. Reverse the item of a list if the item is of odd length string otherwise keep the item as is!.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
reverse_odd_length = []
for name in names:
    if len(name)%2==0:
        reverse_odd_length.append(name)
    else:
        reverse_odd_length.append(name[::-1])
print(reverse_odd_length)    
#with using comprehension.
_reverse_odd_length = [name if len(name) % 2 == 0 else name[::-1] for name in names]

###########################################################
#11.reverse the item of list only if it is string,otherwise keep as is.
data = ['hello', 123, 1.2, 'world', True, 'python']
d = [item[::-1] if isinstance(item, str) else item for item in data]

##########################################################################
#zip():-it is function used to iltrate or loop over mutliple collection at once.
#12. ADD the item of two list using zip.
#with out zip and comprehension.
a = [1,2,3,4]
b = [5,6,7,8]
total = []
if len(a)==len(b):
    for i in range(len(a)):
        total.append(a[i]+b[i])
print(total)

#with using zip and  without comprehension.
_total = []
for x,y in zip(a,b):
    _total.append(x+y)
print(_total)

#with using zip and comprehension.
print([x+y for x,y in zip(a,b)])



# Raise to the power of list index
a = [1, 2, 3, 4, 5]
i = [value ** index for index, value in enumerate(a)]

#create a list of tuples of city name and its temparature details
cities = [ 'bangalore', 'chenai', 'delhi']
temparature = [25,30,35]
cities_temp = [value for value in zip(cities,temparature)]#('bangalore,25),('chenai',30),('delhi',35)
print(cities_temp)
#Raise to the power of list index
a = [1, 2, 3, 4, 5,2,4,5,6,1] #[1**0,2**1,3**2,4**3,5**4]
#[1,2,9,64,625]
power_index = []
for i in range(0,len(a)):
    power_index.append(a[i]**i)
print(power_index)
#---------------------------------------------
power_index_ = []
for index,value in enumerate(a):
    power_index_.append(value**index)
print(power_index_)
#---------------------------------------------
print({value**index for index,value in enumerate(a)})
###################################################################################
################
matrix = [[1, 2, 3,3], [4, 5, 6,6,], [8,7, 8, 9]]
#o/p [1, 2, 3, 4, 5, 6, 7, 8, 9]
flattend_matrix = []
for row in matrix:
    for item in row:
        flattend_matrix.append(item)
print(flattend_matrix )
#multiple for in comprehension
print([item for row in matrix for item in row])
    




'''
#1.Write a program to print list of numbers between the range 1 to 20.
#2.WAPTP list of charactor in given string,  greet = 'Hello World'
#3.WAPTP list of square numbers,which are present given list,numbers = [1,2,3,4,5]
#4.# Building a list of first_name and last_name from full_names
##    full_names = ["steve jobs", "bill gates", "john doe", "tim cook"]
#5.list of even numbers between range of 1 to 20
#6.WAPTP a list of polindromes from given list.
#names =['steve','eve','john','anna','stella','bob']
#7.Filtering out those names which are less than 6 characters
#names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
#8. Filtering all the languages which starts with 'p'
#languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
#9. Build a list with only even with even length string
#names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
#10. Reverse the item of a list if the item is of odd length string otherwise keep the item as is!.
#names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
#11.reverse the item of list only if it is string,otherwise keep as is.
#data = ['hello', 123, 1.2, 'world', True, 'python']
#12. ADD the item of two list using zip.
#a = [1,2,3,4]
#b = [5,6,7,8]
#13 Raise to the power of list index
#l = [1,2,3,4,5]


'''














