k,l=map(int,input().split())
a=list()
for i in range(k,l+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        a.append(i)
print(len(a))
