k=input()
a=len(k)
k=list(map(int,k.split("/")))
if a!=10:
    print("no")
else:
    print("yes" if ((k[0]<=31) and (k[1]<=12)) else "no")
