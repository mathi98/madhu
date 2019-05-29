k=int(input())
prod=1
a=0
while(k):
    a=k%10
    prod=prod*a
    k=k//10
print(prod)
