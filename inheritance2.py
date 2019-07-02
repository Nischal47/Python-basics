class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
class Student(Person):
    #Using __init__ inside child will disable the inheritance property
    def __init__(self,fname,lname):
        pass  #pass is used if no properties are added
    
    def printname(self):
        print(self.fname,self.lname)#This will cause error
x=Student("Ram","Parsad")
x.printname()