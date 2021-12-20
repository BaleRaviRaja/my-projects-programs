n=int(input("Enter the number = "))
sq=n*n
count=0
while(n>0):
    if(n%10!=sq%10):
        print("Not Automorphic number")
        count=1
        break
    n=n//10
    sq=sq//10
if(count==0):
    print("Automorphic number")