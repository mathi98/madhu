k=int(input())
a=[int(x) for x in input().split()]
b=0
if k==len(a):
    for i in range(0,k):
        for j in range(i+1,k):
            b=a[i]^a[j]
print(b)
