k=input()
l=list(map(int,input().split()))
a=0
b=0
for i in range(0,len(l)):
    if l[i]%2==0:
        a+=1
        c=l[i]
    else:
        b+=1
        c1=l[i]
if a==1:
    print(c)
else:
    print(c1)
