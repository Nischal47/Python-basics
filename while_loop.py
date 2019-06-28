i=0
while i<10:
    print(i)
    i+=1


#We can use break to get out of loop
j=0
while j<10:
    print(j)
    if j==5:
        break
    j+=1

#we can use continue to jump to next itteration
k=0
while k<10:
    k+=1
    if k%2==0:
        continue
    print(k)
