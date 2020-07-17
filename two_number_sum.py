#1st method time=O(n^2) as two traversal of array elements,
#space=o(1) as no new space is been used, so space is constant
def doubleloop(arr, targetnumber):
    for i in range(len(arr)-1):
        for j in range(i+1 , len(arr)):
            if arr[i]+arr[j] == targetnumber:
                return [arr[i], arr[j]]
    return []

#second method time=o(n) as one traversal of arr elements, space=O(n) as one
#complete hashtable is been made of n elements of array
def hashmeth(arr, targetnumber):
    numhash={}
    for num in arr:
        probablenum=targetnumber- num
        if probablenum in numhash:
            return [probablenum, num]
        else:
            numhash[num]='true'
            print(numhash)
    return []

# third method , time=O(nlogn) as log for sorting algo and n for traversing once through array
#space=O(1) as there is no extra space is taken by creating any new element
def sortnsearch(arr, targetnumber):
    arr.sort()
    print(arr)
    left =0
    right = len(arr)-1
    while left < right:
        if arr[left]+arr[right]== targetnumber:
            return [arr[left], arr[right]]
        elif arr[left]+arr[right] > targetnumber:
            right=right-1
        elif arr[left]+arr[right] < targetnumber:
            left=left+1
    return []
        
        


arr=[-1 , 2, 15 , 7, 8 ,5]
num=10
sum=doubleloop(arr,num)
sum1=hashmeth(arr,num)
sum2=sortnsearch(arr,num)
print(sum)
print("Hash method", sum1)
print("SortnSearch", sum2)
