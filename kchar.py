k,l,m=map(str,input().split(" "))
m=int(m)
a=0
for i in range(len(k)):
    if k[i]!=l[i]:
        a+=1
if a==m:
    print("yes")
else:
    print("no")
