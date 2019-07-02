#Self parameter is used to access variables that belongs to the class. 
#Note:-It can be named anything. It is first parameter of function inside class. Self is generally used .
class car:
    def __init__(self,name,company): 
        self.name=name
        self.company=company
    def color(self,x):
        print(x +" "+self.name+" "+self.company)
p1=car("f12","ferrari")
p1.color("Red")
p2=car("Huracan","Lamborgini")
p2.color("Yellow")
