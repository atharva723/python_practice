#lambda func to add 15 to passed num
f1=lambda a:a+15
#square and cube any num
f2=lambda num:(num**2,num**3)
#multipy 2 arguments
f3=lambda y,x:y*x
#add two numbers
f4=lambda y,x:y+x
#solve expression a**2+b**2+2*a*b
f5=lambda a,b: a**2+b**2+2*a*b
#solve expression 2*a+3*b+4*c
f6=lambda a,b:2*a+3*b+4*c
#return last element of any sequence
f7=lambda a:a[-1]
#program to check palindrome
f8=lambda a:a[::]==a[::-1]
#convert negative to positive
f9=lambda i:abs(i)
#check if character is present in string or not
f10=lambda d,a:d in a


####homework
l=[1,2,3,4]
print([i**2 for i in l])

def pow(li,p=[],i=0):
    if i>=len(l):
        return p
    p.append(l[i]**2)
    i+=1
    return pow(l,p,i)


f=lambda l:[i**2 for i in l]
