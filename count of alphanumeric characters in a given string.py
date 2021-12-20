def solve(str):
    count=0
    for i in str:
        if(i.isalpha() or i.isnumeric()):
            count+=1
    return count
n=input("Enter alphanumeric characters = ")
print(solve(n))