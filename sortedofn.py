k=int(input())
a=list(map(int,input().split()))
s=sorted(a)
if s==a:
    print("yes")
else:
    print("no")
