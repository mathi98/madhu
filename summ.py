k=int(input())
a=0
b=0
while(k>0):
    a=k%10
    b=b+a
    k=k//10
print(b)
