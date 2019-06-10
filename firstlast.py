k=list(map(str,input().split()))
for i in range(1,len(k)):
    if i!=len(k)-1:
        k[i]=k[i][::-1]
print(*k)
