k,l=map(int,input().split())
a=[int(x) for x in input().split()]
a.sort()
for i in l:
    if i>k:
        print(i)
        break
