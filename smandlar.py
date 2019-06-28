k=int(input())
a=list(map(int,input().split()))
if len(a)==k:
    b=max(a)
    c=min(a)
    d=b-c
print(d)
