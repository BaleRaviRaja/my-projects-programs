bnum=int(input("enter any binary number = "))
dnum=0
base=1
while(bnum>0):
    rem=bnum%10
    dnum=dnum+base*rem
    bnum=bnum//10
    base=base*2
print("desimal number of given number is  = ",dnum)