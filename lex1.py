k=int(input())
l=list(map(str,input().split()))
a=sorted(l,key=len)
for i in range(len(a)-1):
    if len(a[i])==len(a[i+1]) and a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
print(*a)
