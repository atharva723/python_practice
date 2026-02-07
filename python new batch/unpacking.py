#### Unpacking --> unpacking is done to divide collection into individual value

#### unpacking
##def unpacking(a,b,c):
##    return a,b,c
##
##print(unpacking(*[1,2,3]))



#### 1)WAP numbers frok 1 to 20 without using any loop
##a,*num=range(0,21)  ## cutomize unpacking
##print(num)
##
##
##def countup(i=1):  ## recursion 
##    if i<=20:
##        print(i)
##        i+=1
##        countup(i)
##
##countup()




#### 2)print the number 10 to 1 even number
##def even(i=10):
##    if i>=1:        ##recursion termination condition
##        if i%2==0:
##            print(i)
##        i-=1
##        even(i)
##even()
        


#### 3)wap to extract only string of value from given list withot using any loop
data=['hello',12,'apple',3.4,True,'Bye']

