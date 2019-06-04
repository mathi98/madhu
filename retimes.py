k=list(map(int,input().split()))
n=k[len(k)-1]
a=[i for i in input().split()]
for i in a:
    if a.count(str(i))==n:
        print(i)
        break
