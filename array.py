#Bubble sort in array
from array import *
#creating an empty array to store the integer
x=array('i',[])

#store element into the array
print("how many elements?", end =' ')
n= int(input())

for i in range(0, n):
    print("enter element", end=' ')
    x.append(int(input()))

print("Original array:", x)

#bubble sort algo [17, 25, 13, 28, 37, 21])

flag=0
for i in range(0, n):
    for j in range(n-1-i):
        if(x[j]>x[j+1]):
                t=x[j]
                x[j]=x[j+1]
                x[j+1]=t
                flag= 1
    if flag== 0:
        break
    else:
        flag= 0
print("Sorted array:",x)
    
                


