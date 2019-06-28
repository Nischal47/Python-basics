#in python funcrtion is defined by keyword def
def add(a,b): #a and b are parameters
    return a+b
c=add(4,5)
print(c)

#default value 
def add_default(e=0,f=0):
    return e+f
c=add_default()
d=add_default(3,2)
print(c)
print(d)

#We can pass lists, tuples, sets and dictionaries as parameters
mylist=["CPU","GPU","RAM","SSD"]
def myfunction(a):
    for x in a:
        print(x)
myfunction(mylist)