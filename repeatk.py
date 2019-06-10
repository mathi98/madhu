k,l=map(int,input().split())
a=[int(x) for x in input().split()]
if l in a:
    print("yes",a.count(l))
else:
    print("no")
