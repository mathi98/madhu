k=input()
a=0
for i in range(0,len(k)):
    for j in range(i+1,len(k)):
        if k[i]==k[j]:
            a+=1
if a>=1:
    print("yes")
else:
    print("no")
