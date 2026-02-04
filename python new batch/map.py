#find if a given list of string starts with "A"
name=['alex',"Steve","anna",'Henry',"john","Akon"]
print(list(filter(lambda a:a[0] in "Aa",name)))
#to convert positive num
n=[1,-45,-3,5]
print(list(map(abs,n)))


#raise theeir power based on index
n=[1,2,3,4]
y=lambda a:a[1]**a[0]
print(list(map(y,enumerate(n))))


#length of each name in list
l=["wipro","TCS","microsoft","ubisoft"]
print(list(map(len,l)))


#length having length less than 5
print(list(filter(lambda n:len(n)<5,l)))

#filter palindrome
name=['alex',"Steve","anna",'Henry',"john","Akon"]
print(list(filter(lambda a:a[::]==a[::-1],name)))
