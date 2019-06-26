k=int(input())
a=0
for i in range(0,k+1):
    for j in range(0,k+1):
        if i*3==k:
            a+=1
        elif i*7==k:
            a+=1
        elif (i*3)+(i*7)==k:
            a+=1
if a>=1:
    print("yes")
else:
    print("no")
