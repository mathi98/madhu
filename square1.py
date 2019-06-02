k=int(input())
a=0
while k>0:
    b=k%10
    a=a+b**2
    k=k//10
print(a)
