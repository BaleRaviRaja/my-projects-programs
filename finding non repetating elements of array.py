size=int(input("ENTER ARRAY SIZE = "))
arr=[ ]
a=[]
for i in range(size):
    element=int(input())
    arr.append(element)

for i in set(arr):
    if arr.count(i)==1:
        a.append(i)
print("non repetating elements are",a)