ar1=list(map(int,input("Enter array 1 = ").split()))
ar2=list(map(int,input("Enter array 2 = ").split()))
c=0
x=len(ar2)
for i in ar2:
    if i in ar1:
        c+=1
if(c==x):
    print("Array 2 is subset of Array 1")
else:
    print("Array 2 is not subset of Array 1")