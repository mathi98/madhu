k=int(input())
l=list(map(int,input().split()))
a=1
b=[]
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        a+=1
    else:
        b.append(a)
        a=1
b.append(a)
print(max(b))
