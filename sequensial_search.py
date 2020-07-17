from array import *
#Sequential search example
x=array('i',[])

print("how many elements?:", end=' ')
n=int(input())

for i in range(0, n):
    print("Enter new element of array:")
    x.append(int(input()))

print("Original array:", x)

print("Enter element to be searched in array:", end=' ')
m=int(input())
flag=0

for i in range(n):
    if (x[i]== m):
        flag=1
        print("Element found at:", i+1)
        
    
if flag==0:
    print("Elemet not found")

