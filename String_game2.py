#split,join,swapcase example
sample="Akhilesh is a moody person"
##str=input("Enter string seperated by space").split()
##str1='-'.join(str)
##print("Original",str)
print("Modifiled",sample)
str3=sample.swapcase()
print("swapcase eg",str3)
str4=sample.title() 
print("Title eg",sample)
id=50
name = 'akhilesh'
salary= 100000
print("salary={1},id={0},name={2}".format(id,name, salary))
print("to know the nature of character entered by user")
str=input("enter one character: ")
ch=str[0]
alphanum=0
alpha=0
num=0
for ch in str:
    if ch.isalpha():
        alpha=alpha+1
    elif ch.isnumeric():
            num=num+1
    elif ch.isalphanum():
            num=num+1
    else:
        print("This is space")

if(alphanum>=1 and alpha>=1):
    print("Alpha")
elif (num>1):
    print("Numeric")
    
    

