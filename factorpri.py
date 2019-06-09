j=int(input())
a=[]
for i in range(2,j):
    if j%i==0:
        a.append(i)
for i in a:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
