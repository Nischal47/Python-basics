#String are array like other languages although character data type is not available in python
a="Hello World"
print(a[4])

print(a[1:6])#Substring from 1 to (6-1)=5

print(a.strip())#Removes whitespaces from beginning and end

#lower()->lowercase & upper()->uppercase
print(a.lower())

#format can be used to use combine integer and strings
b=5
txt=(a+" "+"{}")
print(txt.format(b))

string="Python {}"
version=3.7
print(string.format(version))