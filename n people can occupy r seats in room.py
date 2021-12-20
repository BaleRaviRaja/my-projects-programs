n=int(input("enter no of students = "))
s=int(input("enter no of seats = "))
nfact=1
sfact=1
a=n-s
for i in range(1,n+1):
    nfact=nfact*i
for j in range(1,a+1):
    sfact=sfact*j
print("total no of ways are = ",(nfact//sfact))
