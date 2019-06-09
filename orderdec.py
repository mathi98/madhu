k=int(input())
a=list(map(int,input().split()))
b=list(set(a))
b.sort(reverse=True)
c=[]
d=[]
e=0
for i in b:
    c.append(a.count(i))
while e<len(c):
    f=c.index(max(c))
    d.append(b[f])
    c[f]=0
    e=e+1
print(*d)
