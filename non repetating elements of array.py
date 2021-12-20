arr=int(input("Enter size of array = "))
a=[]
for i in range(arr):
    x=int(input("enter "+str(i)+"element = "))
    a.append(x)
print(a)
for j in set(a):
    if(a.count(j)==1):
        print(j,end=" ")