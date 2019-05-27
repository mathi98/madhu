k,l=map(int,input().split())
a=0
m=k*l
b=max(k,l)
for i in range(1,b+1):
    if k%i==0 and l%i==0:
        a=i
print(int(m/a))
