k=int(input())
a=[int(x) for x in input().split()]
if k%2!=0:
    l=(k-1)//2
    b=sorted(a[0:l])
    c=sorted(a[l:])
    s=b+c[::-1]
    print(*s)
else:
    l=k//2
    b=sorted(a[0:l])
    c=sorted(a[l:])
    s=b+c[::-1]
    print(*s)
    
