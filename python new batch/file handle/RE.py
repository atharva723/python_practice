import re
from re import sub
print(re.findall("gr[ea]y","sky is either grey or gray"))


print(re.findall("[\d]","the cost of book is 100rs"))


print(re.findall("[a-z]+","hello WORLD How"))
print(re.findall("[A-Z]+","hello WORLD How"))
print(re.findall("[a-zA-Z]+","hello WORLD How"))



print(re.findall("[1-6]","pen cost 12rs"))



print(re.findall(r'\bh[a-z]+',"hello world happy birthday"))


print(re.findall(r"\b[PJ][a-z]+","Python is easy Programming Language and Java"))


print(re.findall(r"\b[a-zA-Z]+y","Happy brithday"))

print(re.findall(r"\b[A-Z]+\b","This is PYTHON Regex PROGRAM "))
print(re.findall(r"[a-zA-Z]+.pdf\b","downloading text.pdf and offer.pdf"))


print(len(re.findall(r"\s","1928:273:73763 ,      WARNING  ")))

with open("sample A13.log") as file:
    total=0
    for i in file:
       total+=len(re.findall(r'\s',i))
    print(total)
    
count_blank=lambda path,word:sum([len(re.findall(word,i))for i in open(path)])

cap_letter=lambda path:sum([len(re.findall('[A-Z]+',i)) for i in open(path)])
sd="648 this string starts with 12 and ends with 658946555 78"
print(re.findall('[0-9]',sd))

print(re.findall(r"[0-9]",sd))

print(re.findall(r'\b[0-9]{3}\b',sd))
sd1="pincode of banglore is 560002 and number is 45893212318"
print(re.findall(r"\b\d{6}\b",sd1))



print(re.findall('(python|java)','the python and java '))





print(len(re.findall('[a-z]','Hello WORLD welcome to PYTHon')),len(re.findall('[A-Z]','Hello WORLD welcome to PYTHon')))

_format=['00:00:00','23:59:59','24:00:00',"1:59:00"]
for i in _format:
    print(re.findall(r'(?:0[0-9]|1[0-9]|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)',i))



line="how are you.... ??, what... ?do you do?"
print(len((re.findall(r'\?',line))))
print(len((re.findall(r'\.',line))))
print(len((re.findall(r'\*',line))))



print(sub("[aeiou]","*",line))

line="how are you....   ??, wh a  t... ?do you do?"
print(sub("[\?\.]",'~',line))


print(sub(r'\band\b','&','python and java are easy'))




print(sub(' ',r'\n',line ))



sent="he helps the community and she is new to operations"
print(re.findall('he[a-z]+|he',sent))







