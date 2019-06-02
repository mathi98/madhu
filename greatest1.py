k,l=map(int,input().split())
list=[]
range1=max(k,l)
for i in range(1,range1):
    if (k%i==0) and (l%i==0):
        list.append(i)
a=sorted(list)
print(a[-1])
