def solve(arr,n):
    count=1
    for i in range(n-1):
        flag=1
        for j in range(i+1,n):
            if(arr[i]<=arr[j]):
                flag=0
                break
            if(flag):count+=1
    return count
n=int(input("Enter size of array = "))
arr=list(map(int,input("Enter element = ").split()))
print(solve(arr,n))

