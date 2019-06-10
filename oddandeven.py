
k=input()
a=[]
b=0
for i in range(0,len(k)-1):
    l=int(k[i])+int(k[i+1])
    if l%2!=0:
        b+=1
    else:
        a.append(b)
        b=0
    a.append(b)
c=max(a)
if c==0:
    print(0)
else:
    print(c+1)
