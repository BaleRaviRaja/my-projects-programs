fn=int(input("enter first number numerator = "))
fd=int(input("enter first number denominator = " ))
sn=int(input("enter second number numerator = "))
sd=int(input("enter second number denominator = "))
if(fd==sd):
    print("resultant fraction is = " + str(fn+sn)+'/'+str(fd))
else:
    print("resultant fraction is = " + str((fn*sd)+(sn*fd))+'/'+str(fd*sd))
