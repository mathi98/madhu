k,l=map(int,input().split())
a=[int(x) for x in input().split()]
b=a[0:k]
c=a[k:]
d=[]
for i in b:
    if i in c:
        d.append(i)
        c.remove(i)
print(*d)
