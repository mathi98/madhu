k=input()
a=k.lower()
b=0
c=0
for i in range(len(k)):
    if a.count(a[i])>b:
        b=a.count(a[i])
        c=i
print(k[c])
