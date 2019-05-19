a,b=input().split()
a=int(a)
b=int(b)
for i in range(a,(b-1),1):
    a=a+1
    if(a%2!=0):
        print(a,end=" ")
