x= list(input("Enter set of characters = "))
print(x)
lv=[]
lc=[]
for z in x:
    if (z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u'):
       lv.append(z)
    else:
      lc.append(z)
print("vowels are = ",lv )
print("consonents are = ",lc)
