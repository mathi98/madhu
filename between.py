k=int(input())
a,b=input().split()
a=int(a)
b=int(b)
if(k in range(a+1,b)):
    print("yes")
else:
    print("no")
