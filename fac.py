k=int(input())
a=2
b=[]
c=[]
for a in range(a,k+1):
    i=2
    while i<a:
        if a%i==0:
            break
        i+=1
    if a==i:
        b.append(a)
for i in b:
    if k%i==0:
        c.append(i)
for i in range(0,len(c)-1):
    print(c[i],end=" ")
print(c[len(c)-1])
            
