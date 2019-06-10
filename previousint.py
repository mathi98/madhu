k=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in range(1,len(a)):
    if a[i]%a[i-1]==0:
        b.append(a[i])
print(*b)

