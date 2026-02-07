from re import findall
 Count total number of Upper case and Lower case letters
def count(sentence):
    """Returns a tuple of uppercase and lowercase letters count in a given string"""
    sentence = "Hello World Welcome To Python"
    upper_case = findall(r'[A-Z]', sentence)
    lower_case = findall(r'[a-z]', sentence)
    return (upper_case, lower_case)
# --------------------------------------------------------------------------
# Write a program to count the number of white spaces in a given string
def spaces(sentence):
    sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"
    spaces = findall(r'\s', sentence)
    return len(spaces)


# --------------------------------------------------------------------------
# Meta Character "+" (matches 1 or more occurances of previous expression)
# --------------------------------------------------------------------------
# matches any digit between 0-9 as long as there is a match
re=findall(r'[0-9]+', 'The cost of the book is Rs.100')
print(re)
# matches one or more occurances of "n" between two "a"'s
re1 = findall(r'an+a', 'annnnnnnnnnna')
print(re1)
# matches lower case alphabets between as long as there is a match
findall(r"[a-z]+", "hello worLD Welcome To Python Programming Pyt123on")
# --------------------------------------------------------------------------
# Sum all the numbers in the below string.
# --------------------------------------------------------------------------
word = "Pytho12nReg567exp2" # 1 + 2 + 5 + 6 + 7 + 2
total = 0
numbers = findall(r'[0-9]', word)
for number in numbers:
    total += int(number)

# Adding 12 + 567 + 2
word = "Pytho12nReg567exp2"
total = 0
numbers = findall(r'[0-9]+', word)
for number in numbers:
    total += int(number)
# --------------------------------------------------------------------------
# Meta Character "?" (matches 0 or 1 occurance of previous expression)
# --------------------------------------------------------------------------
print(findall(r'colou?r', "what color do you like"))

print(findall(r'https?://', 'https://www.google.com'))

print(findall(r'https?://', 'http://www.google.com'))

print(findall(r'July?', "Jul the 26th day"))

print(findall(r'an?a', "ana"))

print(findall(r'an?a', "anna"))
# --------------------------------------------------------------------------
# Negation "^"
# --------------------------------------------------------------------------
# Matches everything apart from numbers between 0-9
print(findall(r'[^0-9]', 'The cost of the book is Rs.100'))

# Matches everything apart from alphabets 'a', 'b', 'c' and 'd'
findall(r'[^abcd]', 'abcdefg hijkab')

# Matches everything apart from numbers between 0-9
findall(r'[^0-9]+', 'The cost of the book is Rs.100')

findall(r'[^abcd]+', 'abcdefg hijkab')

# Match only those characters excepts digits
word = '@hello12world34welcome!123'
findall(r'[^0-9]', word)

# Count the number of special characters in the below string
sentence = 'hello@world! welcome!!! Python$ hi26 how are you & where are you?'
findall(r"[^a-zA-Z0-9_\s]", sentence)
# -------------------------------------------------------------------------------------------------
# Starts with "^" and ends with "$"
# -------------------------------------------------------------------------------------------------
#print(findall(r"^hello", "hello world"))

findall(r"^hello", "world hello")

findall(r"hello$", "world hello")

findall(r"hello$", "hello world")

findall(r'hello$', 'hello world welcome to python')

# string starts with "hello" and ends with "hello" (meaning exactly one word is allowed in the str)
findall(r"^hello$", "hello")
# -------------------------------------------------------------------------------------------------
# Word Boundary (\b) The expression should be a word boundry 
# (Transition between non-word character to word character or word character to non-word character)
# ------------------------------------------------------------------------------------------------
# starts with word boundry
findall(r"\bday", "what a beautiful day today is")

# ends with word boundry
findall(r"day\b", "what a beautiful day today is")

# starts and ends with word boundry
findall(r"\bday\b", "what a beautiful day today is")

# Regular expression which matches words that starts with "h"
findall(r"\bh[a-zA-Z0-9_]+", 'hello world hi hello universe how are you happy birthday')

# Regular expression which matches words that starts with "P or J"
findall(r"\b[PJ][a-zA-Z0-9_]+", 'Python is a programming language. Python is easier than Java')

# Regular expression which matches words that ends with "y"
findall(r"[a-zA-Z0-9_]+y\b", 'hello world hi hello universe how are you happy birthday feeling very sleepy flying')

#