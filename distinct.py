k=int(input())
a=[int(x) for x in input().split()]
b=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]<a[j]:
            b+=1
print(b)
