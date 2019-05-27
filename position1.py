k=input()
l=''
m=''
for i in range(0,len(k),1):
    if i%2==0:
        l+=k[i]
    if i%2==1:
        m+=k[i]
print(l,m)
