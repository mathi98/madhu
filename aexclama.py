k,l=map(int,input().split())
a=1
b=1
for i in range(1,k+1):
    a=a*i
for i in range(1,l+1):
    b=b*i
print(a//b)
