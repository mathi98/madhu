k=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in range(0,len(a)):
    if a[i]<k:
        b.append(a[i])
        b.sort()
print(*b)
