a,b=map(int,input().split())
for num in range(a+1,b):
    r=0
    t=num
while(num>0):
    d=num%10
    r=r+d**3
    num=num//10
if(t==r):
    print(t,end=" ")
