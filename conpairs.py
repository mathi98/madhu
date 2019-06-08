k=int(input())
a=[int(x) for x in input().split()]
b=0
for i in range(0,len(a)-1):
    sum=a[i]+a[i+1]
    b=b+sum
print(b)
