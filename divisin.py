k=int(input())
a=0
for i in range(2,k):
    if k%i==0:
        print("yes")
        a+=1
        break
if a==0:
    print("no")

