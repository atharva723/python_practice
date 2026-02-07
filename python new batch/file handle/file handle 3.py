##with open('sample A13.log') as file:
##    msg=[]
##    d={}
##    for line in file:
##        if line.strip():
##            msg.append(line.split()[2])
##    for a in msg:
##        count=1
##        if a not in d:
##            d[a]=count
##        else:
##            d[a]+=1
##---------------------------------------------------------------
def msgs(path):
    msg=[line.split()[2] for line in open(path) if line.strip()]
    d={ms:msg.count(ms) for ms in msg}
    return print(f"list of messsages\n{msg}\nmessages and count pairs\n{d}")
###################################################################
with open('emp.csv','w') as file:
    file.write('emp_id,ename,gender,salary\n')
    file.writelines(["101,STEVE,male,54000\n",
                     "102,MARIA,Female,58000\n",
                     "103,RAVI,MALE,98244\n"])
