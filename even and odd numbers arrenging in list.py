n=int(input("enter any number = "))
l=[]
le=[]
l0=[]
for i in range(1,n+1):
    x=int(input("enter "+str(i) +" element = "))
    l.append(x)
for i  in l:
    if(i%2==0):
        le.append(i)
    else:
        l0.append(i)
l1=le+l0
print(l1)
