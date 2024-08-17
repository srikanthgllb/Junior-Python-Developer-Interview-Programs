x=[3,6,2,95,74,6,3]
min=x[0]
max=x[0]
n=len(x)
for i in range(1,n):
     if x[i]<=min:
          min=x[i]
     if x[i]>=max:
          max=x[i]
print(min)
print(max)

          
