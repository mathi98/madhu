j=int(input())
k=[int(x) for x in input().split()]
a=[]
if len(k)!=1:
    for i in range(j-1):
        a.append(k[i]|k[i+1])
else:
    a.append(k[0])
print(max(a))
   
