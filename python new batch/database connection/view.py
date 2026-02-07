#---------cretaing database
##import sqlite3
##connect=sqlite3.connect("MY_DATA.db")
##cursor=connect.cursor()
##cursor.execute('''
##CREATE TABLE EMP(
##NAME TEXT ,
##AGE INTEGER,
##SALARY INTEGER)
##
##''')

#---each query should be executed only once or it will throw the error------#


#-------------inserting
##import sqlite3
##connect=sqlite3.connect("MY_DATA.db")
##cursor=connect.cursor()
##cursor.execute('''
##INSERT INTO EMP(NAME,AGE,SALARY) VALUES(?,?,?)''',
##               #('ATHARVA' ,21,34000)
##               #('PRATIK' ,20,4500)
##                #('DAVID' ,34,78000)
##                #('ALWYNN' ,51,99000)
##)
##connect.commit()
##connect.close() 


##import sqlite3
##connect=sqlite3.connect("MY_DATA.db")
##cursor=connect.cursor()
##cursor.executemany('''
##INSERT INTO EMP(NAME,AGE,SALARY) VALUES(?,?,?)''',
##               (('ASHTON' ,28,34400),
##                ('TRAVIS' ,41,84000))
##)
##connect.commit()
##connect.close() 

#--------updating
##import sqlite3
##connect=sqlite3.connect("MY_DATA.db")
##cursor=connect.cursor()
##cursor.executemany('''
##UPDATE EMP
##SET AGE=? 
##WHERE NAME=?
##''',((24,'ATHARVA'),(32,'TRAVIS'))
##)
##connect.commit()
##connect.close() 


###----------EXTRACTING 
##import sqlite3
##connect=sqlite3.connect("MY_DATA.db")
##cursor=connect.cursor()
##Extracted_data=cursor.execute('''
##SELECT *
##FROM EMP
##'''
##)
##
##for i in Extracted_data:
##    print(i)
##connect.commit()
##connect.close() 
##
##
##
