k,l=map(int,input().split(" "))
a,b=map(int,input().split(" "))
c,d=map(int,input().split(" "))
if k==a==c:
    print("yes")
elif l==b==d:
    print("yes")
elif k==l and a==b and c==d:
    print("yes")
else:
    print("no")
