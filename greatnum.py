k=int(input())
a=[int(x) for x in input().split()]
b=max(a)
c=0
d=[]
for i in range(1,b+1):
    c=0
    for j in range(0,len(a)):
        if a[j]%i==0:
            c+=1
    if c==len(a):
        d.append(i)
g=max(d)
print(g)

