n=input("Enter array elaments = ").split()
l=list(n)
k=int(input("Enter no of rotations = "))
for i in range(k):
    x=l.pop(0)
    l.append(x)
print("array after ratations is ", l)