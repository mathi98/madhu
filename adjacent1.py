k=int(input())
a=[int(i) for i in input().split()]
for i in range(0,k-1,2):
    a[i],a[i+1]=a[i+1],a[i]
print(*a)
