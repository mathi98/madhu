k,l=map(int,input().split())
m=list(map(int,input().split()))
a=0
for i in range(0,k):
    if m[i]%2!=0:
        a+=1
        if a==l:
            print(m[i])
