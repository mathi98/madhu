k=int(input())
l=list(map(int,input().split()))
a=[]
b=""
for i in range(k-1):
    c=max(l[i],l[i+1])
    a.append(c)
for i in a:
    b=b+str(i)+" "
print(b.strip())
