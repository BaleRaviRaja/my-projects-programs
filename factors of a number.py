n=int(input("enter a number to find factors "))
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")

