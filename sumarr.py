k=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in range(k):
    c=a[:i+1]
    if sum(c)%2==0:
        b.append(str(sum(c)))
    else:
        b.append(str(a[i]))
print(" ".join(b))
