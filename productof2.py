k,l=map(int,input().split())
a=k*l
b=bin(a)
b=a[::-1]
for i in b:
    if i==" ":
        print(b.index(i)+1)
        break
