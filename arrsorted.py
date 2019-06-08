k=int(input())
a=[int(x) for x in input().split()]
b=sorted(a)
c=[]
for i in range(0,len(b)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c.append(j)
for i in range(len(c)):
    c[i]=c[i]+1
print(*c)
