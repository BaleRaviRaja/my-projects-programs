def getcount():
    l=[]
    s=int(input("Enter size of array = "))
    for i in range(s):
        c=int(input("Enter "+str(i)+" element = "))
        l.append(c)
    d=int(input("Enter element to be searched = "))
    return l.count(d)
print(getcount())
