k,l=map(int,input().split())
list=list(map(int,input().split()))
for i in list:
    if i==l:
        print("Yes")
        break
else:
    print("No")
