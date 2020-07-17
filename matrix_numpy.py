from numpy import *
import sys
#this is to take the product of two matrix
#take two matrix as input
r1,c1=[int(a) for a in input("Enter the row and col for first matrix:").split()]
r2,c2=[int(a) for a in input("Enter the row and col for second matrix").split()]
#test whether the c1 is equal to r2 or not
if (c1 != r2):
    print("Multiplication not possible")
    sys.exit()

print("Enter the element for first matrix:", end=" ")
str1=input()
m1=reshape(matrix(str1), (r1,c1))
print("Enter element for second matrix:", end =" ")
str2=input()
m2=reshape(matrix(str2),(r2,c2))

m3= m1 * m2
print("Product of two matrixes are:", m3)
