k,l=map(int,input().split())
a=[int(i) for i in input().split()]
for i in range(k-1,l-1,-1):
    a.remove(a[i])
print(*a)
