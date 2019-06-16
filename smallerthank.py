k,l=map(int,input().split())
a=[int(x) for x in input().split()]
b=0
if l in a:
    print(k)
else:
    for i in a:
        if i>b and i<k:
            b=i
    print(b)
