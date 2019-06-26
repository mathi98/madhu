k=int(input())
a=list(map(int,input().split()))
b=1
for i in range(k-1):
    if a[i]>a[i+1] and a[i]>=a[i+1]:
        b=1 
print(b)
