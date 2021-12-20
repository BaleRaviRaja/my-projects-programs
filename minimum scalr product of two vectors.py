a=list(map(int,input("Enter array1").split()))
b=list(map(int,input("Enter array2").split()))
a.sort()
b.sort(reverse=True)
s=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(i==j):
            s+=a[i]*b[j]
print("Minimum scalar product of two arrays is = ",s)

