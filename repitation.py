k,l=map(int,input().split())
m=list(map(int,input().split()))
a=0
for i in range(0,len(m)):
    if(m[i]==l):
        a+=1
print(a)
