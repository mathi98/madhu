k,l=map(str,input().split())
count=0
for i in range(0,len(k)):
    if(k[i]!=l[i]):
        count+=1
    else:
        continue
if count==1:
    print("yes")
else:
    print("no")
