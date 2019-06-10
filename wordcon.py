k=int(input())
a=[]
for i in range(k):
    a.append(input())
b=0
for i in range(k-1):
    if a[i]==a[i+1]:
        b=1
        print("yes")
        break
if b==0:
    print("no")

