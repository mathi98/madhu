k=map(int,input().split())
a=[int(x) for x in input().split()]
b=[]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        b.append(abs(a[i]-a[j]))
print(max(b))
