k,l,m=map(int,input().split())
if k+l<=m or k+m<=l or l+m<=k:
    print("yes")
else:
    print("no")
