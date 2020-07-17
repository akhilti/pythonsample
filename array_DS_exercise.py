from array import *
month=['Jan','Feb','Mar','April','May']
expense=[2200,2350,2000,2130,2190]
#Extra_In_Feb=expense[January]-expense[Feb]
print("Extra ",expense)
print("Month",month)
print("extra spent in Feb:",expense[1]-expense[0])
print("Total expense in first quarter:", expense[0]+expense[1]+expense[2])
for i in range(0,len(expense)):
    if(expense[i]==2000):
        print("2000 spent in month:",month[i])
expense.append(1980)
month.append('June')
for i in range(0, len(month)):
    if month[i]=='April':
        expense[i]=expense[i]-200
print("Final month list:",month)
print("Final expense list",expense)
print()
print("Exercise-2")
heros=['spider man','thor','hulk','iron man','captain america']
print("Lengh of the list",len(heros))
heros.append('black panther')
print("Updated list",heros)
heros.remove('black panther')
print("removed black panther", heros)
n=0
for i in range(0,len(heros)):
    if heros[i]=='hulk':
        n=i
        break
heros.insert(n+1,'black panther')
print("Updated list",heros)
heros[1:3]=['doctor strange']
print("sorted list",sorted(heros))
