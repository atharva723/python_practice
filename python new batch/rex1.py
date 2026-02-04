#Regular expression

from re import findall

# --------------------------------------------------------------------------
# Rule: The Match That Begins Earliest (from left to right) Wins
# --------------------------------------------------------------------------
out1 = findall(r"the", "the theory of relativity")
print(out1)
out2 = findall(r"cat", "The dragging belly indicates your cat is too fat")
print(out2)

out3 = findall(r'python', 'python and java are object oriented')
print(out3)

out4 = findall(r'aeiou', 'hello how are you doing anna')
print(out4)

out5 = findall(r'aeiou', 'hello how are you doing anna, aeiou')
print(out5)

# --------------------------------------------------------------------------
# Character class or set
# --------------------------------------------------------------------------
# Matches with both "Smith" and "smith"
# character set is used to match any one of many/several characters
findall(r'[sS]mith', 'smith and blacksmith')
findall(r'[sS]mith', 'Smith and blackSmith')

# Matches "separate" or "saperate"
findall(r'sep[ae]rate', 'seperate')
findall(r'sep[ae]rate', 'separate')

# Matches "grey" and "gray"
findall(r"gr[ea]y", "grey")
findall(r"gr[ea]y", "gray")

# Match any one character in the character set (either a, e, i, o, u)
findall(r'[aeiou]', 'hello how are you doing anna')

# Match either a, b, c, d
findall(r'[abcd]', 'hello world')
findall(r'[abcd]', 'abcdefghijk')

# Matching any number between 0-9
findall(r'[0123456789]', 'The cost of the book is Rs.100')

# Matching HTML headers
findall(r'<h[123456]>', "<h1>")
findall(r'<h[123456]>', "<h2>")
findall(r'<h[123456]>', "<h3>")
findall(r'<h[123456]>', "<h4>")
findall(r'<h[123456]>', "<h5>")
findall(r'<h[123456]>', "<h6>")
# --------------------------------------------------------------------------
# Range "-"
# --------------------------------------------------------------------------
# Matches any number between 0-9
# "-" represents range inside character set
findall(r'[0-9]', 'The cost of the book is Rs.100')

# Matches only lower case letters
findall(r"[a-z]", 'hello HOW ARE YOU')

# Matches only upper case letters
findall(r"[A-Z]", 'hello HOW ARE YOU')

# Matches all upper case and lower case characters
findall(r"[a-zA-Z]", 'hello HOW ARE YOU')

# Matches any number between 1-6
findall(r"<h[1-6]>", "<h1>")
findall(r"<h[1-6]>", "<h2>")
findall(r"<h[1-6]>", "<h3>")
findall(r"<h[1-6]>", "<h4>")
findall(r"<h[1-6]>", "<h5>")
findall(r"<h[1-6]>", "<h6>")
# --------------------------------------------------------------------------
# Count total number of Upper case and Lower case letters
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

print(sum([int(num)for num in findall('[0-9]+',word)]))
