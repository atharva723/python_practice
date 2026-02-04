class Company:
    cname="apple"
    ceo="steve"
    MBL="california"
    def __init__(self,name,eid,phno,gmail,sal):
        self.name=name
        self.eid=eid
        self.phno=phno
        self.gmail=gmail
        self.sal=sal
    def ch_phon(self,new_phno):
        self.phno=new_phno
    @classmethod #it is built in decorator that makes this as class method i.e anyone can change the ceo (it will effect the class member ceo)
    def che_ceo(cls,new_ceo):
        cls.ceo=new_ceo
    def ch_gmail(self,new_gmail):
        self.gmail=new_gmail
    @classmethod
    def ch_loc(cls,new_MBL):
        cls.MBL=new_MBL
    
    @staticmethod  #it is built in decorator that allows any one to access the function as without this object reference will automatically passed as argument
    def greet():
        return "Welcome to APPLE company"
e1=Company("atharva",1021,8291632871,"atharvajadhav2023@gmail.com",2560)
