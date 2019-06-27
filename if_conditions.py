#if else can be done as
a=int(input())
b=int(input())
c=a%2
if a>b:
    print("{} is greater than {}".format(a,b))
elif a==b:
    print("{} and {} are equal".format(a,b))
else:
    print("{} is greater than {}".format(b,a))


#if can be done in single line as
if a>b: print("{} is greater".format(a))

print("{} is even".format(a)) if c==0 else print("{} is odd".format(a))