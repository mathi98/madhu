k=int(input())
a=[]
for i in range(1,k+1):
    if k%i==0:
        if i%2!=0:
            a.append(i)
print(*a)
