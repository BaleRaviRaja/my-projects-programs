s=input("enter any string")
s=s[0:1].upper()+s[1:len(s)-1]+s[len(s)-1:len(s)].upper()
print("string is = ",s)