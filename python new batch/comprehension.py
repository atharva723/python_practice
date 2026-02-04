###comprehension :it is a process of creating new mutable collection with elegent
####way of single line expression as per the syntax of python
####types of comprehension
####list
####set
####dictionary
##
####list comphrehension:-it is a process of ceating a new list with optimized code or in
####single line as per the syntax of python
##
###syntax:
####var_name=[value_to_store for value in collection]
####var_name=[value_to_store for value in collection if condition]
####var_name=[TSB if condition else FSB for value in collection]
####var_name=[value_to_store for items in collection for value in items]
##
##
##
###wapto print list of character
##greet='Hello Word'
##l=[i for i in greet]
##
###waplist of square numbers ,which are present given
####number =[1,2,3,4,5]
####print([a**2 for a in number])
##
##
###wap to get first names from list
####full_name=['steve jobs','bill gates','john doe']
####print([ i.split()[0] for i in full_name])
####print([ i.split()[1] for i in full_name])
##
##
###list of even  number from 1to 20
##print([a for a in range(1,20) if a%2==0])
##
##
###list of palindrom
##l=['steve','eve','anna','john','stella','bob']
##print([i for i in l if i[::-1]==i[::]])
##
##
###filter words less than 6 charcter
##w=['apple','google','yahho',"flipkart"]
##print([i for i in w if len(i)<6])
##
##
###filter language that starts from p
##lang=['python',"Java",'PHP',"perl",'Ruby',"PYTHON"]
##print([i for i in lang if i[:1:] in "pP"])
##
###wap a list with only even with even length string
##name=['apple','yahoo','facebook','yelp','flipkart','gamil','instagram','microsoft']
##print([name[i] for i in range(len(name)) if i%2==0 ])
##
##
##
##
##
###reverse item of list if length of word is odd else keep as it is
##name=['apple','yahoo','facebook','yelp','flipkart','gamil','instagram','microsoft']
##print([i[::-1]if len(i)%2!=0 else i[::] for i in name])
##
##
###reverse if string
##data=['hello',12,1.2,'world']
##print([i[::-1]if type(i)==str else i for i in data])
##
#add the items of a lists
a=[1,2,3,4]
b=[5,6,7,8]
print([a[i]+b[i] for i in range(len(a))])
print([i+j for i,j in zip(a,b) ])

#raise the power to the elements index number
a=[1,2,3,4,5]
print([a[i]**i for i in range(0,len(a))])

a2={1,2,3,4,5}
print([v**i for i,v in enumerate(a2) ])

#get output
mat=[[1,2,3,4,5],[6,7,8,9],[10,11,12,13,15]]
print([a for i in mat for a in i])


#zip:-it is a built in function or built in iterator which is used to iterate or access
##values from multiple collection simultaneously
##zip doesnt aware sturcture to display its value so for that we can access the values by using typecasting or using for loop
for v in zip('abc',[1,2,3,4],{9,10}):
    print(v)
for v1,v2,v3 in zip('abc',[1,2,3,4],{9,10}):
    print(v1,v2,v3)
##NOTE= zip will stop iteration or value access at shortest length of the collection
#ENUMERATE():- enumerate is a built in function or iterator used to get the index and value pairs from any collection
##enumerate is also one of the iterator ,we can access the values using type casting and for loop
for v in enumerate('abc'):
    print(v)
for v in enumerate({2,3,4,5}):
    print(v)
for v in enumerate({2:4,6:8}):
    print(v)

#SET COMPREHENSION:- it is a proccess of creating new set with single line of expression as per the syntax
# syntax for set comprehension is same as list comprehension but here we must change the boundaries to {}.


#DICTIONARY COMPREHENSION:-
#it is a phenomenon of creating new output dictionarty by reducing the number of instruction taken to do the required operation
#syntax {key:value for value in collection}
        #{key:value for value in collection if cond}
sentence="this is a bunch of words"
print({i:len(i) for i in sentence.split()})



#flip key and value pair
d={'a':1,'b':2,'c':3}
print({d[i]:i for i in d})

#count no of each character in a string
sent="hello world welcome to python hello hi world welcome to python "
print({i:sent.count(i)for i in sent})

#word and count pair
sent="hello world welcome to python hello hi world welcome to python "
print({i:sent.count(i)for i in sent.split()})


#cretae dict pair city and population
city=['Tokyo','Delhi','Shanghai']
popu=['38,101,,000',"12,22,450","5,00,000"]
print({city[i]:popu[i] for i in range(0,len(city))})


#wap to create dict of country and dail code
dial_code=[(86,"china"),(91,"INDIA"),(1,"USA"),(55,'BRAZIL'),(7,"russia")]
print({i[1]:i[0] for i in dial_code})
print({country:code for code,country in dial_code})

#wap build a dict price more than 200
price={"ACME":45.21,"AAPL":612.5,"IBM":205.21,"HPQ":37.45}
print({i:price[i]for i in price if price[i]>200})




#LIMITATIONS of comprehension:-
'''
>we cant customize the comprehension syntax
>we cant use while loop ,elif nested if statements in comprehension
> we cant initialize the variables in comprehension
>it is APPLICABLE ONLY FOR MUTABLE COLLECTIONS
'''

















    

