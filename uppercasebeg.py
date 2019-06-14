k,l=input().split()
l=int(l)
a=""
for i in range(len(k)-1):
    if (i+1)%k==0:
        a+=k[i].upper
    else:
        a+=k[i]
print(a)
    
