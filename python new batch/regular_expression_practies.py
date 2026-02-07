s1="the theory of relativity"

s2="The dragging belly indicates your cat is too fat"

s3='python and java are object oriented'

s4='hello how are you doing anna'

s5='hello how are you doing anna, aeiou'
# --------------------------------------------------------------------------
# Matches with both "Smith" and "smith"
s6='Smith and blackSmith'

# Matches "separate" or "saperate"

# Matches "grey" and "gray"

# Match any one character in the character set (either a, e, i, o, u)
s7='hello how are you doing anna'

# Match either a, b, c, d

# Matching any number between 0-9
s8='The cost of the book is Rs.100'

# Matching HTML headers
# Matches any number between 0-9
s9='The cost of the book is Rs.100'

# Matches only lower case letters
s10='hello HOW ARE YOU'

# Matches only upper case letters
s11='hello HOW ARE YOU'

# Matches all upper case and lower case characters
s12='hello HOW ARE YOU'

# Matches any number between 1-6
# --------------------------------------------------------------------------
# Count total number of Upper case and Lower case letters
sentence = "Hello World Welcome To Python"


# --------------------------------------------------------------------------
# Write a program to count the number of white spaces in a given string
sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# matches one or more occurances of "n" between two "a"'s
s13='annnnnnnnnnna'
# matches any digit between 0-9 as long as there is a match
s14='The cost of the book is Rs.100'


# matches lower case alphabets between as long as there is a match
s15="hello worLD Welcome To Python Programming Pyt123on"
# --------------------------------------------------------------------------
# Sum all the numbers in the below string.
# --------------------------------------------------------------------------
word = "Pytho12nReg567exp2" # 1 + 2 + 5 + 6 + 7 + 2

# Adding 12 + 567 + 2

# --------------------------------------------------------------------------
# Meta Character "?" (matches 0 or 1 occurance of previous expression)
# --------------------------------------------------------------------------
s16="what color do you like"

s17='https://www.google.com'

s18='https?://', 'http://www.google.com'

s19="Jul the 26th day"


# --------------------------------------------------------------------------
# Negation "^"
# --------------------------------------------------------------------------
# Matches everything apart from numbers between 0-9
s20='The cost of the book is Rs.100'

# Matches everything apart from alphabets 'a', 'b', 'c' and 'd'


# Matches everything apart from numbers between 0-9
s21='The cost of the book is Rs.100'



# Match only those characters excepts digits
word = '@hello12world34welcome!123'

# Count the number of special characters in the below string
sentence = 'hello@world! welcome!!! Python$ hi26 how are you & where are you?'
# -------------------------------------------------------------------------------------------------
# Starts with "^" and ends with "$"
# -------------------------------------------------------------------------------------------------
s22='Hello world'


# string starts with "hello" and ends with "hello" (meaning exactly one word is allowed in the str)
WB= "what a beautiful day today is"#extact day

# -------------------------------------------------------------------------------------------------
# Word Boundary (\b) The expression should be a word boundry 
# (Transition between non-word character to word character or word character to non-word character)
# ------------------------------------------------------------------------------------------------

# ends with word boundry

# starts and ends with word boundry

# Regular expression which matches words that starts with "h"
s23='hello world hi hello universe how are you happy birthday'

# Regular expression which matches words that starts with "P or J"
s24='Python is a programming language. Python is easier than Java'

# Regular expression which matches words that ends with "y"
s25='hello world hi hello universe how are you happy birthday feeling very sleepy flying'

# print only those words starting with vowel character
sentence = "hello hi american english and indian ocean united states"

# Matches only Capital Letter words
s26="This is PYTHON programming LANGUAGE and REGEX"

# Matches only lower case words
s27="This is PYTHON programming LANGUAGE and REGEX"

# Matching only pdf files
s28="downloading apple.pdf to downloads folder"

# Different Combintations
line = "03/22 08:51:06 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available."
# ------------------------------------------------------------------------------------------------------------
# Count the number of white spaces in the file
# -------------------------------------------------------------------------------------------------------
# Count the number of Capital Letter words in the file
# -------------------------------------------------------------------------------------------------------
# Count the number of INFO, TRACE, WARNING, EVENT messages in the file
# -------------------------------------------------------------------------------------------------------
# Matches all digits
# -------------------------------------------------------------------------------------------------------
sd="654 this string is starting with 12 and ending with numbers 289423784612 890"

# Matches whole numbers

# Matches sequence of all 3 digit pattern

# Matches exactly 3 digit numbers

# Matches the string that ends with 3 digit number

# Matches excatly 6 digit numbers
sd1='Pincode of Bangalore is 560001 and the number is 1234567890'

# Matches the string that starts with 3 digit number
sd3="654 this string is starting with and ending with numbers 289423784612"

# Phone Number pattern (4DIGITS-3DIGITS-3DIGITS)
phno='456-9832-098'

# Regular Expression - IP Addresses
ips = ['10.1.2.3', '127.0.0.0', '199.99.9.9', '199.9.9999.9', '127-0-0-0']

# matching only 800 and 900 numbers

# Extract only 4 digit numbers from the string
sd4="Copyright 1998. All rights reserved"

# Regular Expression - PAN Number
sentence = "my pan number is ABCDE1234X and the other number is XYZTR3104J id is 123XYZTR3104J89"

# Regular expression for matching only 3 letter words in the given string
sentence = "hello hi how are you what is your name he is older than me how old are you"
# o/p ['how', 'are', 'you', 'how', 'old', 'are', 'you']

# --------------------------------------------------------------------------
# Meta Character "*" (matches 0 or more occurances of previous expression)
# --------------------------------------------------------------------------

# Regular expression for matching the words which starts with "he"
sentence = "he helps the community and he is the hero of the day"
# -------------------------------------------------------------------------------------------------------
# Groups ( )
# -------------------------------------------------------------------------------------------------------------
# Matches either "python" or "java"
py='python and java are object oriented'

# Regular Expression for Matching Inbox, Inbox(1), .... Inbox(N)

# Regular expression for matching the words which either starts with "he" or "se"
sentence = "he helps the community and he is the hero of the day she sells sea shells on the sea shore"

# Match only those lines that were logged in year 98 
# Regular Expression - YYYY-MM-DD date format
_dates = ['2019-01-02', '2019-13-02', '2019-12-26', '26-08-2019', '20-19-20', '2019-12-31', '2019-12-32']

# Regular Expression - 24hr time format
_formats = ['00:00:00', '23:59:59', '24:00:00', '1:59:20', '12:9:10', '10:20:8']

# Regular Expression - 24hr time format
_formats = ['00:00:00', '23:59:59', '24:00:00', '1:59:20', '12:9:10', '10:20:8']
# ------------------------------------------------------------------------------------------------------------
# escaping meta characters
# ------------------------------------------------------------------------------------------------------------
# Count the number of occurances of question marks ("?") in the below string
line = "hello there.. how are you? how is it going?? what are you doing? ... "

# Count the number of occurances of dots(".") in the below string
line = "hello there..... how are you? how is it going?? what are you doing? ... "

# Count the number of occurances of stars ("*") in the below string
line = "hello there..... how are you? *** how is it going?? what * are you  ** doing? ... "
#---------------------------------------------------------------------------------------
# Replacing patterns
# ------------------------------------------------------------------------------------------------------
# Replace all vowels with "*"
sentence = "hello world welcome to python"

# Replace all occurances of digits with "*"

# Replace all occurances of special characters with "*"
sentence = 'hello#$%world welcome@!#$%to python*&^%'
#Replace "And" with "&"
sentence = "Java and Python are programming languages"
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# Replace whitespaces with newline character in the below string
sentence = "Hello world welcome to python"
# ------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# dot "." matches with everything
# ------------------------------------------------------------------------------------------------------
