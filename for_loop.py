#For loop in python differ from other programming languages
#It works like itterator in other object oriented languages


thisdictionary={
    "Name": "Nischal",
    "Age": 21,
    "Course": "BSc.CSIT"
}
#This will get values
for x in thisdictionary.values():
    print(x)
#This will get keys
for x in thisdictionary:
    print(x)
for x in thisdictionary:
    print(str(x)+" "+str(thisdictionary[x]))
#this can also be done as
for x,y in thisdictionary.items():
    print(x,y)


# we can use range in for loop as
for x in range(5): #start from 0 to 5-1
    print(x)
for x in range(1,5): #start from 1 to 5-1
    print(x)
for x in range(1,10,2): #start from 1 to 10 with itteration +2
    print(x)

#Nested loop
for x in range(6):
    for y in range(x):
        print(x,y)