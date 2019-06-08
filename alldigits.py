k,l=map(str,input().split())
l=int(l)
a=0
for i in range(l):
    if str(i) in k:
        a+=1
if a==l:
    print("yes")
else:
    print("no")
