k,l=map(int,input().split())
a=[int(x) for x in input().split()]
b=[]
for i in range(0,len(a)):
    if a[i]<l:
        b.append(a[i])
        b.sort()
print(*b)
