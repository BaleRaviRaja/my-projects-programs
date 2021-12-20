a=int(input("enter first number = "))
b=int(input("enter second number = "))
c=int(input("enter third number = "))
d=int(input("enter fourth number = "))
if(a>b and a>c):
    print("first number is biggest")
elif(b>c and b>d):
    print("second number is biggest")
elif(c>d):
    print("third number is biggest")
else:
    print("fourth number is biggest")