size=int(input("Enter size of string = "))
max=0
count=0
str=input("Enter binary elements with spaces = ")
arr=list(str)
for i in range(0,size):
    if arr[i]=='1':
        count=count+1
    elif(arr[i]=='0'):
        count=0
    if count>max:
            max=count
print("maximum length of signal is =  ",max)

