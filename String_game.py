print(r"Welcome \rto \aPython world \b, \nlets play \rsome \tescape \vcharacter game")
str="Core Python"
for i in range(len(str)):
    print(str[i])
print()
for i in str[::-1]:    
    print(i, end ="")
print()

str1=input("Enter main string")
str2=input("Enter sub string")
m= str1.find(str2, 0, len(str1))
##print(n+1)
##print(str1,id(str1))
##str1=str1.rstrip()
##print(str1,id(str1))
##print(str1.lstrip(),id(str1))
n=str1.index(str2)
print("String found at :",m+1)
#find all position of a substring in a main string
flag=0
i=0
while i<len(str1):
    n=str1.find(str2,i,len(str1))
    if(n!=-1):
        print("Substring found at pos:",n+1)
        flag=1
        i=n+1
    else:
        i=i+1

if flag==0:
    print("Substring not found")
count= str1.count(str2)
print("No of times this substring occured:", count)
str3=str1.replace('h','Dil')
print("New string",str3)
