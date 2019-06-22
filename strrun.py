
k=input()
a=0
b=""
c=a+1
d=1
while c<len(k):
    if k[a]==k[c]:
        d=d+1
    else:
        b=b+k[b]+str(d)
        a=c
        d=1 
    c=c+1 
b=b+k[b]+str(d)
print(b)
