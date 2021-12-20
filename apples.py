n = int(input("Enter how amny apples you want = "))
m1 = int(input("Enter no of apples in lot form shop A = "))
p1 = int(input("Enter coat price of each lot in shop A = "))
m2 = int(input("Enter no of apples in lot form shop B = "))
p2 = int(input("Enter coat price of each lot in shop B = "))
min_cost = -1
i = 0
while m1 * i <= n:
    count2 = n - i*m1
    if count2%m2 == 0:
        cost = int(p1 * i + p2 *(count2/m2))
        if cost < min_cost or min_cost == - 1:
            min_cost = cost
    i += 1
if min_cost != -1:
    print("minimum cost price of apples is ",min_cost)
else:
    print("Invalid inputs")
