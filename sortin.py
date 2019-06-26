k,l=map(int,input().split())
a=[int(x) for x in input().split()]
b=a[:l]
c=a[l:]
b.sort()
c.sort(reverse=True)
print(b,c)
