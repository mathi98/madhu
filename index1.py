k=int(input())
a=[int(i) for i in input().split()]
for i in range(0,k):
    if((i+1)==a[i]):
        print(i)
        break
