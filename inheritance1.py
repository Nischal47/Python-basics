class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

#Child class is defined by passing parent class as Parameters
class Student(Person):  
    def printname(self):
        print(self.fname, self.lname)
x=Student("Ram","Parsad")
x.print()
