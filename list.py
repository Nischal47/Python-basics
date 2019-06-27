alist=[5,2,3]#list is ordered and changeble
#list is accessed like
print(alist[0])
#value in list can be changed like
alist[2]=7
print(alist[2])
#For accessing every elements in list
for x in alist:
    print(x)
#We can copy list like
blist=alist.copy()
print(blist)
#tO CHECK LIST  
if 7 in alist:
    print("Yes")
#for list length
print(len(alist))
#We can append in list by using append command
alist.append("oranges")
if "oranges" in alist:
    print("Yes")
#Can be deleted by function remove pop and del
alist.remove("oranges")
alist.pop()
del alist[1]
print(alist)

#We can clear list as
alist.clear()
print(alist)
