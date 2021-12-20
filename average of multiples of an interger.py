def average():
    n=int(input("Enter any number = "))
    m=int(input("Enter no of multiples you want = "))
    a=[]
    for i in range(1,m+1):
        x=i*n
        a.append(x)
    avg=sum(a)/m
    return avg
print(average())

