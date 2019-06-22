k=list(input().split())
if len(k)>1:
    for i in range(len(k)):
        if k[i]=='and':
            k[i-1],k[i+1]=k[i+1],k[i-1]
    print(*k)
else:
    print(*k)
