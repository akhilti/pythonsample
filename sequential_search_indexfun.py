from array import *
x=array('i',[])
print("how many elements?", end=' ')
n=(int(input()))
for i in range(n):
    print("Enter new element")
    x.append(int(input()))

print("Original array :", x)

print("Enter element to be searched", end=' ')
m=(int(input()))
try:
    pos=x.index(m)
    print("Element fount at position", pos+1)
except valueError:
    print("Element not found in array")
    


