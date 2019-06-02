k,l=map(int,input().split())
a=k*l
b=[]
for i in range(1,a+1):
    if i%k==0 and i%l==0:
        b.append(i)
print(min(b))
