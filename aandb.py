k=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[]
for i in a:
    if i in b:
        c.append(i)
n=set(c)
n=sorted(n)
print(*n)
