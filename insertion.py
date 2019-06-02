k,l=map(int,input().split())
input()
a=""
b=list(map(int,input().split()))
c=list(map(int,input().split()))
for i in c:
    b.append(i)
    c=max(b)
    a=a+str(c)+" "
print(a.strip())
