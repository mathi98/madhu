k=str(input())
m=len(k)
a=m//2
if(m%2!=0):
    for i in range(0,1):
        if(i==a):
            print("*",end="")
        else:
            print(k[i],end="")
else:
    for i in range(0,1):
        if i==a-1 or i==a:
            print("*",end="")
        else:
            print(k[i],end="")
