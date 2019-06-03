k,l=map(str,input().split())
a=int(k/2)
b=int(l**0.5)
if (a*2==0 and b*b==l):
    print("yes")
else:
    print("no")
