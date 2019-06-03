k,l=map(str,input().split())
l=int(l)
a=map(k)
b=k
for i in range(0,l):
    b=b[-1]+b[:a-1]
print(b)
