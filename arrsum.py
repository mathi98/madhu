k,l=map(int,input().split())
a=list(map(int,input().split()))
for i in range(0,k-1):
    if a[i]+a[i+1]==l or a[i]==l:
        print("yes")
        break
else:
    print("no")
