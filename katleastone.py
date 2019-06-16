k,l=map(int,input().split())
a=[]
b=0
for i in range(k):
    a.append(input())
c=["a","e","i","o","u"]
for i in c:
    if any(j in c for j in i):
        b+=1
if b>=k:
    print("yes")
else:
    print("no")
