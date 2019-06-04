k=map(int,input().split())
a=[int(x) for x in input().split()]
b=[]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        if a[i]-a[j]!=0:
             b.append(abs(a[i]-a[j]))
print(min(b))
