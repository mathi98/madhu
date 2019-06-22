k=input()
k.strip()
num=len(k)
for i in range(2,num):
    if num%i==0:
        print("yes")
        break
else:
    print("no")
