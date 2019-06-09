k=int(input())
a=[int(x) for x in input().split()]
b=max(a)
c=0
d=[]
for i in range(b,1000):
    c=0
    for j in range(0,len(a)):
        if i%a[j]==0:
            c+=1
    if c==len(a):
        d.append(i)
e=min(d)
print(e)
