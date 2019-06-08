j=int(input())
k=[int(x) for x in input().split()]
a=k[0]
for i in range(1,len(k)):
    a=a|k[i]
print(a)
