arr=[1,2,3,4,5]

print(sum(arr))  #15

print(sum(arr,10)) #25

print(sum(arr,-10))  #5 


#input from user
def array_from_user():
     array=[]
     n=int(input("enter the no of elements in array"))

     for i in range(n):
           element=input(f"enter the element {i+1}")
           array.append(element)
     return array
new_array=array_from_user()
print("the array is",new_array)
