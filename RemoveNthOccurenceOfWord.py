mylist=["geeks","for","geeks","geeks"]
count=0
word="geeks"
n=3

for i in range(0,len(mylist)-1):
     if (mylist[i]== word):
          count=count+1
          print("1")
          if (count==n):
               del mylist[i]
print(mylist)
