k=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        b.append(a[i])
    else:
        b.append(a[i+1])
print(sum(b))
