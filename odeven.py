k=int(input())
a=list(map(int,input().split()))
b=1
for i in a:
    b=b*i
if b%2==0:
    print("even")
else:
    print("odd")
