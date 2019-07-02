class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.name=self.fname+self.lname
class Student(Person):
    
    def __init__(self,fname,lname,RollNO):#We can add properties in child class like this. 
        #Using __init__ inside child will disable the inheritance property. To re-enable it parent is called.
        Person.__init__(self,fname,lname)
        self.RollNO=RollNO
    
    def printname(self):
        print("Name :",self.name)
        print("RollNO :",self.RollNO)
x=Student("Ram","Parsad","1")
x.printname()
    