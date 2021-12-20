s,n = map(int,input().split())
sum=s
for i in range(1,n):
    prev=sum-1
    sum+=prev
print("total no of mints kids have",sum)