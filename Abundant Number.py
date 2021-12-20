n=int(input("enter any number = "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum>n):
    print("Abundant Number")
else:
    print("not an Abundant Number")
