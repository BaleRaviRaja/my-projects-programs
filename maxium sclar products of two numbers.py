n=int(input("Enter the size of Array: "))
print("Enter the elements of First Array")
arr1=list(map(int,input().split()))
print("Enter the elements of Second Array")
arr2=list(map(int,input().split()))
arr1.sort()
arr2.sort()
sumVariable=0
for i in range(0,n):
    sumVariable+=arr1[i]*arr2[i]
print("Maximum scalar product of two vectors :",sumVariable )
