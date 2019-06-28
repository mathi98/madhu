k=input()
a=len(k)
b=0
for i in range(len(k)-1):
    if k[i]!=k[a-i-1]:
        b=b+1 
if b<=1:
    print("yes")
else:
    print("no")
