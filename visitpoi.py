k,l=map(int,input().split())
a=[]
b=0
for i in range(0,k):
    a.append(list(map(int,input().split())))
for i in range(0,len(a)):
    if a[i][1]==l:
        b+=1
if b==0:
    print("no")
else:
    print("yes")
