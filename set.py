thisset={1,2,3}#Set is collection of unordered and unindexed with no duplication.
#vlaues can be printed as
for x in thisset:
    print(x)
#VAlUES Are added by add() and multiple values by update()
thisset.add(4)
print(thisset)
thisset.update([5,6,7])
print(thisset)
#deleted by pop discard remove functions as
thisset.remove(1)#doesn't produce error message when item(unindexed) not found
thisset.discard(9)#doesn't produce error message when item(unindexed) not found
print(thisset.pop())#set is unordered so last element is unknown so return value is checked
print(thisset)
