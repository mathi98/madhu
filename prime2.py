k=int(input())
a=0
for i in range(2,k//2+1):
    if(k%i==0):
        a=1
if(a==0):
    print("yes")
else:
    print("no")
