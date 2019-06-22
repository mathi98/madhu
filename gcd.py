k,l=map(int,input().split())
a=min(k,l)
b=1
for i in range(1,a+1):
    b*=i
print(b)
