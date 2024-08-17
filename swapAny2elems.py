#Approach 1 simple swap

mylist=[23,35,78,248,6]

pos1=int(input('enter the position of element inList'))
pos2=int(input('enter the another position of element inList'))

mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)

#Approach 2 pop() function
mylist=[11,22,33,44]
pos1=int(input('enter the position of element inList'))
pos2=int(input('enter the another position of element inList'))

fe=mylist.pop(pos1) #22
se=mylist.pop(pos2-1)#11,33,44

mylist.insert(pos1,se)
mylist.insert(pos2,fe)

print(mylist)

# Approach using tuple
