arr=list(map(int,input("Enter array elements").split()))
x=list(dict.fromkeys(arr))
print("Elements of array",arr)
print("Elements of array with out duplicates",x)
print("Count of distinct elemnts",len(x))


