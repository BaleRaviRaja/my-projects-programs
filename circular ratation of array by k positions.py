n=input("Enter array elaments = ").split()
l=list(n)
k=int(input("Enter no of rotations = "))
k=k%len(l)
for i in range(k):
    x=l.pop(-1)
    l.insert(0,x)
print("array after ratations is ", l)