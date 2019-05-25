k=input().split()
a=len(k)
min=k[0]
for i in range(1,a):
    if(min>k[i]):
        min=k[i]
print(min)
        

