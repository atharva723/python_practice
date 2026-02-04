##
###nested  for loop
##writing a for loop inside a another for loops is called as nested for loop
##syntax
##for value1 in collection:
##    for value2 in collection or value1:
##        STATEMENT BLOCK
##
##outer for loop will take the first value and get inside the inner for loop, inner for loop will have it
##first value , untill the inner for loop is completely executed it will not go back to outer for loop
##Example:
##  #wap to extract characters present in string one by one those strings are present inside the given list
##l1=["apple","google","TCS"]
##l2=[]
##for i in l1:
##    for a in i:
##        l2.append(a)
##
##
##print(l2)
##using while loop
##l1=["apple","google","TCS"]
##i=0
##while i<len(l1):
##    j=0
##    while j<len(l1[i]):
##        print(l1[i][j])
##        j+=1
##    i+=1


#wap to get output for input
##l1=[12,'hai',89,6.7,'python']
##vowels={}
##for i in l1:
##    if type(i)==str:
##        count=0
##        for a in i:
##            if a in "aeiouAEIOU":
##                count+=1
##        vowels[i]=count
##print(vowels)


#wap to get output using slicing
##l2=[12,'hai',89,'program',6.7,'python']
##l3=set()
##for i in l2:
##    if type(i)==str:
##        rev=''
##        for a in i:
##            rev=a+rev
##        print(rev)
##            
##    else:
##        pass

#wap to get output
##st='python is very easy'
##l1=st.split()
##di={}
##print(l1)
##for i in l1:
##    count=0
##    for a in i:
##         count+=1
##    di[i]=count
##print(di)
    
##n=5
##for i in range(1,n+1):
##    for j in range(i):
##        print(i,j)


#pattern program
##n=5
##for i in range(1,n+1):
##    for j in range(i):
##        print('*',end=' ')
##    print()

##n=5
##for i in range(n,0,-1):
##    for j in range(i):
##        print('*',end=' ')
##    print()
