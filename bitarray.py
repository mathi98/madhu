j=int(input())
k=[int(x) for x in input().split()]
a=k[0]
for i in range(0,len(k)):
    b=a&k[i]
print(b)
