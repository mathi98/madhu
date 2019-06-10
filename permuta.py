k=int(input())
a=[int(x) for x in input().split()]
for i in range(1,len(a)):
    if a[i]-a[i-1]==1:
        print("yes")
        break
    else:
        print("no")
        break
