def gcd(k,l):
    a=[]
    for i in range(1,max(k,l)):
        if k%i==0 and l%i==0:
            a.append(i)
    b=len(a)
    return b 
c,d=map(str,input().split())
l=len(c)
k=len(d)
if gcd(l,k)==1:
    print("yes")
else:
    print("no")
