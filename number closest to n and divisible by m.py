def solve(s,n) :
    q = n//m
    n1 = m * q
    n2 = (m * (q + 1)) if (n * m) > 0 else(m * (q-1))
    if (abs (n-n1) < abs (n-n2)):
        return n1
    else:
        return n2
n=int(input("Enter first number = "))
m=int(input("Enter second number = "))
print(solve(n,m))
