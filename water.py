
k=int(input())
l=[]
a=0
for i in range(k):
    l.append(list(map(int,input().split())))
if k==1 and l[0]==[1]:
    print(l)
else:
    for i in range(k):
        for j in range(k):
            if l[i][j]==1:
                if i==0 and j==k-1:
                    if(l[i][j-1]==0 and l[i+1][j]==0):
                        a+=1
                    elif i==0 and j==0:
                        if l[i][j+1]==0 and l[i+1][j]==0:
                            a+=1
                    elif i==k-1 and l[i][j-1]==0 and l[i][j+1]==0 and l[i+1][j]==0:
                        a+=1
                    elif i==k-1 and j==k-1:
                        if l[i-1][j]==0 and l[i][j-1]==0:
                            a+=1
                    elif i==k-1 and l[i][j-1]==0 and l[i][j+1]==0 and l[i-1][j]==0:
                        a+=1
                    elif i!=0 and i!=k-1 and (l[i[j+1]==0] and l[i+1][j]==0 and l[i-1][j]==0 and l[i][j-1]==0):
                        a+=1
print(c)
