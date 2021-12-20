n=list(map(int,input("Enter array elements = ").split()))
count_odd=0
count_even=0
for i in n:
    if i%2==0:
       count_even=count_even+1
    else:
       count_odd=count_odd+1
print("Even elements:",count_even)
print("Odd elements:",count_odd)