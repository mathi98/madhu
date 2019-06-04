k,l=map(int,input().split())
a=[int(x) for x in input().split()]
for i in range(0,len(a)):
    if a[i]==l:
        print(i+1)
        break
