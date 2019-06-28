k=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
i=0
j=k-1
c=1 
k=k-1 
while k>=0:
    if a[i]==b[j]:
        c=1 
    else:
        c=0
        break 
    i+=1 
    j-=1 
    k-=1 
print("yes" if c==1 else "no")
