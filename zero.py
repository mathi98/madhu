k=int(input())
a=input()
b=""
c=""
for i in range(len(a)):
    if a[i]=="1":
        b=b+a[i]+" "
    elif a[i]=="0":
        c=c+b
        b=""
print(c.strip())
