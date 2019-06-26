k=int(input())
a=[int(i) for i in input().split()]
b=a.count(0)
for i in range(b):
    a.remove(0)
    a.append(0)
print(a)
