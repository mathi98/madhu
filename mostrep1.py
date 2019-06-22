k=input()
a=[]
for i in k:
    if i!=" ":
        a.append(k.count(i))
b=max(a)
c=""
for i in k:
    if k.count(i)==b and i not in b:
        c=c+i 
print(b,c)
