k=int(input())
a=[int(i) for i in input().split()]
b=1 
for i in range(0,k-2,2):
    if a[i]<a[i+1] and a[i+1]>a[i+2]:
        b=b+2 
    elif a[i]<a[i+1] and a[i+1]>a[i+2]:
        b=b+2 
    else:
        break
if b==k:
    print("yes")
else:
    print("no")
