n=int(input("enter any number = "))
l=[]
for i in range(1,n+1):
    x=int(input("enter "+str(i) +" element = "))
    l.append(x)
l.sort()
print("biggest of given numbers",l[-1])
print("second biggest number",l[-2])
print("smallest number",l[0])
print("enterd list is = ",l)
print("reverse of list is = ",l[::-1])

