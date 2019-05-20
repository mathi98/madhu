n,a,b=map(int,input().split())
z=0
i=0
while(n>i):
    z=z+a
    a=b+a
    i=i+1
print(z)
