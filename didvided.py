k=int(input())
a=0
for i in range(1,k):
    b=k//i
    if k%i==0 and b%2==1:
        print(i)
        a+=1
        break
if a==0:
    print(k)
