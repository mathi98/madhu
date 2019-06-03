k=int(input())
n=0
for i in range(k):
    a,b=map(int,input().split())
    if a<b:
        n+=1
print(n)
