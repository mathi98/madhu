k=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(1):
    for j in range(i,k):
        b.append(str(sum(a[:j+1])))
print(" ".join(b))
