k=[str(x) for x in input().split()]
a=""
for i in k:
    if len(i)>len(a):
        a=i
for i in k:
    if a==i:
        print(i)
        break
