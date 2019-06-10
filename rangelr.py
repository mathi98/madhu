k,l,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i in a:
    if i>=l and i<=m:
        print(i)
        break
