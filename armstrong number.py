n=input("enter any number = ")
sum=0
m=int(n)
while(m>0):
    r=m%10
    sum=sum+r**len(n)
    m=m//10
if(int(n)==sum):
    print("arm strong number")
else:
    print("not an arm strong number")