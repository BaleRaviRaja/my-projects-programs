n=int(input("enter any number"))
l=[]
for i in range(1,n+1):
    a=n%10
    l.append(a)
    n=n//10
sum(l)
if(n//sum(l)==0):
    print("harshad number")
else:
    print("not harshad number")

