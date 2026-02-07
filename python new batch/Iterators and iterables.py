# Iterable:
"""
1. Anything that can be iterated or looped over is called iterable in Python.
2. All iterables have a special method call __iter__
3. String's, List's, Tuple's, Set's, Dictionary's, file objects and generator's are
iterables.
4. All iterables can be passed to the built-in iter() function to get an iterator
from them.
5. An iterator is an object that implements __next__,
which is expected to return the next element of the iterable object that returned
it,
and raise a StopIteration exception when no more elements are available.
Any iterator can be passed to next() function to get the next item.
6. Iterators does not have length. They do not know how long they are.
7. Iterators do not have length can not be indexed. You can only call next() method
to get
the next item.
8. Generators are iterators, enumerate objects are iterators, zip function is an
iterator file objects are iterators,
9. * Generators.
* Generator Expressions.
* enumerate
* map
* filter
* zip
* reversed
* csv.reader() functions returns an iterator object
"""
# Iterators are Lazy Iterables. i.e. they dont determine what their next item is
#until you
#ask them for it
# Iterator Protocol
# Let's Consider a for Statement
# for item in obj:
# Statements
'''
number=10 #we can't able to looper or iterated it becouse integer object is not a
iterable
f=10.5 #we can't able to looper or iterated it becouse float object is not a
iterable
for value in number:
print(value)
>>error
iterable
1. Anything that can be iterated or looped over is called iterable in Python.
greet = 'Hello world'
numbers = [1,2,3,4,5,6]
for char in greet:
print(char)
for number in numbers:
print(number)
for item in enumerate(greet):
print(item)
for values in zip(greet,numbers):
print(values)
ex:

all collection data types and range(),zip(),enumerate(),file objects and generators
objects
are iterables
2. All iterables have a special method call __iter__
'''
#-------------------------------------------------------
'''
iterator:
1.iterators are the iterables.
2.we can iterate or loop over them.and!!!
3.all the iterators have a special method called __iter__ along with that it has
__next__
method also.
4.ex:- zip(),enumerate(),file objects and generators objects,map,
difference between iterators and iterables.
all the iterators are iterables but all the iterables are  not iterators.
all the iterables have only __iter__ method
all the iterators have a special method called __iter__ along with that it has
__next__
method also.
iterables haveing the length but iterator don't have length..
'''

#########################

# Iterable:
"""
1. Anything that can be iterated or looped over is called iterable in Python.
2. All iterables have a special method call __iter__
3. String's, List's, Tuple's, Set's, Dictionary's, file objects and generator's are iterables.
4. All iterables can be passed to the built-in iter() function to get an iterator from them.
5. An iterator is an object that implements __next__,
which is expected to return the next element of the iterable object that returned it,
and raise a StopIteration exception when no more elements are available.
Any iterator can be passed to next() function to get the next item.
6. Iterators does not have length. They do not know how long they are.
7. Iterators do not have length can not be indexed. You can only call next() method to get
the next item.
8. Generators are iterators, enumerate objects are iterators, zip function is an iterator file objects are iterators,
9. * Generators.
   * Generator Expressions.
   * enumerate
   * map
   * filter
   * zip
   * reversed
   * csv.reader()  functions returns an iterator object
"""

# Iterators are Lazy Iterables. i.e. they dont determine what their next item is until you
#ask them for it

# Iterator Protocol
# Let's Consider a for Statement

# for item in obj:
    # Statements


number=10 #we can't able to looper or iterated it becouse integer object is  not a iterable
f=10.5 #we can't able to looper or iterated it becouse float object is  not a iterable
for value in number:
    print(value)
>>error
iterable
1. Anything that can be iterated or looped over is called iterable in Python.
greet = 'Hello world'
numbers = [1,2,3,4,5,6]

for char in greet:
    print(char)
for number in numbers:
    print(number)

for item in enumerate(greet):
    print(item)
for values in zip(greet,numbers):
    print(values)

ex:
'''
all collection data types and range(),zip(),enumerate(),file objects and generators objects
are iterables'''

2. All iterables have a special method call __iter__

iterator:
'''    
1.iterators are the iterables.
2.we can iterate or loop over them.and!!!
3.all the iterators have a special method called __iter__ along with that it has __next__
  method also.
4.ex:- zip(),enumerate(),file objects and generators objects,map,

difference between iterators and iterables.
all the iterators are iterables but all the iterables not iterators.
all the iterables have only __iter__ method
all the iterators have a special method called __iter__ along with that it has __next__
method also.
iterables haveing the length but iterator don't have length.. 

 
'''







'''
#Iterable:-
st='steve'
lst=[1,2,3,4]
tp=(5,6,7)
s={2,4,6,7}
d={'a':1,'b':2,'c':3}
l=range(1,10)
e=enumerate(st)
z=zip(lst,tp)
#genetors
#file object
#map
#filter
'''
#--------------------------------
'''#Iterators
e=enumerate(st)
z=zip(lst,tp)
#genetors
#file object
#map
#filter
#Iterators
#iterators are iterables.
#all the iterators are iterables but not all the iterables are iterators .
for item in e:
print(item)
for item in e:
print(item)
for item in e:
print(item)
print('hii')
for item in st:
print(item)
for item in st:
print(item)
for item in st:
print(item)
'''
'''
shell code
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit
(AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
=== RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py ===
>>> for char in st:
print(char)
s
t
e
v
e
>>> for i in lst:
print(i)
1
2
3
4
>>> for t in tp:
print(t)
5
6
7
>>> for el in s:
print(el)
2
4
6
7
>>> for k in d:
print(k)
a
b
c
>>> l
range(1, 10)
>>> for i in range(1,10):
print(i)
1
2
3
4
5
6
7
8
9
>>> for item in enumerate(st):
print(item)
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
>>> e
<enumerate object at 0x000001B2E55957C0>
>>> for item in e:
print(item)
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
>>> z
<zip object at 0x000001B2E55A5100>
>>> for item in z:
print(item)
(1, 5)
(2, 6)
(3, 7)
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l
range(1, 10)
>>> dir(l)
['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'count', 'index', 'start', 'step', 'stop']
>>> e
<enumerate object at 0x000001B2E55957C0>
>>> dir(e)
['__class__', '__class_getitem__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__',
'__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__']
>>> a=10
>>> for i in a:
print(i)
Traceback (most recent call last):
File "<pyshell#38>", line 1, in <module>
for i in a:
TypeError: 'int' object is not iterable
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
'__getnewargs__', '__gt__', '__hash__', '__index__', '__init__',
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__',
'__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__',
'__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__',
'__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__',
'__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
'__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
'__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length',
'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
>>> e
<enumerate object at 0x0000023135CFFEC0>
>>> for item in e:
print(item)
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
>>> e
<enumerate object at 0x0000023135CFFEC0>
>>> d
{'a': 1, 'b': 2, 'c': 3}
>>> s
{2, 4, 6, 7}
>>> z
<zip object at 0x0000023135CF5600>
>>> len(st)
5
>>> e
<enumerate object at 0x0000023135CFFEC0>
>>> len(e)
Traceback (most recent call last):
File "<pyshell#50>", line 1, in <module>
len(e)
TypeError: object of type 'enumerate' has no len()
>>> len(z)
Traceback (most recent call last):
File "<pyshell#51>", line 1, in <module>
len(z)
TypeError: object of type 'zip' has no len()
>>> for i in e:
print(i)
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
>>> for i in e:
print(i)
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
>>> next
<built-in function next>
>>> next(z)
(1, 5)
>>> next(z)
(2, 6)
>>> next(z)
(3, 7)
>>> next(z)
Traceback (most recent call last):
File "<pyshell#61>", line 1, in <module>
next(z)
StopIteration
>>> next(z)
Traceback (most recent call last):
File "<pyshell#62>", line 1, in <module>
next(z)
StopIteration
>>> st
'steve'
>>> next(st)
Traceback (most recent call last):
File "<pyshell#64>", line 1, in <module>
next(st)
TypeError: 'str' object is not an iterator
>>> dir(e)
['__class__', '__class_getitem__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__',
'__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__']
>>> dir(st)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust',
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
>>> next(e)
(0, 's')
>>> next(e)
(1, 't')
>>> next(e)
(2, 'e')
>>> next(e)
(3, 'v')
>>> next(e)
(4, 'e')
>>> next(e)
Traceback (most recent call last):
File "<pyshell#72>", line 1, in <module>
next(e)
StopIteration
>>> next(tp)
Traceback (most recent call last):
File "<pyshell#73>", line 1, in <module>
next(tp)
TypeError: 'tuple' object is not an iterator
>>> z
<zip object at 0x0000020BCC339D80>
>>> st
'steve'
>>> next(z)
(1, 5)
>>> next(z)
(2, 6)
>>> next(z)
(3, 7)
>>> for i in z:
print(i)
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
>>> for i in z:
print(i)
(1, 5)
(2, 6)
(3, 7)
>>> e
<enumerate object at 0x000001EAAC215100>
>>> next(e)
(0, 's')
>>> next(e)
(1, 't')
>>> next(e)
(2, 'e')
>>> next(e)
(3, 'v')
>>> next(e)
(4, 'e')
>>> next(e)
Traceback (most recent call last):
File "<pyshell#90>", line 1, in <module>
next(e)
StopIteration
>>> for i in e:
print(i)
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
>>> for i in e:
print(i)
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
>>> next(e)
Traceback (most recent call last):
File "<pyshell#96>", line 1, in <module>
next(e)
StopIteration
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
hii
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
hii
s
t
e
v
e
s
t
e
v
e
s
t
e
v
e
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
(0, 's')
(1, 't')
(2, 'e')
(3, 'v')
(4, 'e')
hii
s
t
e
v
e
s
t
e
v
e
s
t
e
v
e
>>>
= RESTART: C:/Users/Trainer/AppData/Local/Programs/Python/Python39/deco.py
>>> '''
