n=int(input("enter number of purchases = "))
k=int(input("Enter no of candies sold = "))
a=int(input("Enter no of candies in jar = "))
for i in range(1,n+1):
    if(k==0):
        print("Invalid input")
        print("no of candies in the jar is ",a)
    else:
        print("no of candies sold in "+str(i)+ " tranction = ",k)
        print("no of candies in the jar after "+str(i)+" tranction = ",abs(a-k))
        a = a - k