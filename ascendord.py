k=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
s=sorted(b)
c=[]
for i in s:
    d=b.index(i)
    c.append(a[d])
print(*c)
