n=(input("enter any string").lower())
count=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
if(count==0):
    print("no vowels found")
else:
    print("total no of vowels are = ",count)