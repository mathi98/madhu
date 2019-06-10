k,l=map(int,input().split())
a=[]
for i in range(k):
    a.append(input())
if a.count(a[i])==l:
    print("yes")
else:
    print("no")
