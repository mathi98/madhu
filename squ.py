k,l=map(int,input().split(" "))
a=0
for i in range(k,l+1):
    for j in range(1,i+1):
        if j**2==i:
            a+=1
print(a)
