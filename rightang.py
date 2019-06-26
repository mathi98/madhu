k,l,m=map(int,input().split())
if k==max(k,l,m):
    a=l 
    b=m
elif l==max(k,l,m):
    a=k 
    b=m 
else:
    a=k 
    b=l 
if max(k,l,m)**2==(a**2)+(b**2):
    print("yes")
else:
    print("no")
