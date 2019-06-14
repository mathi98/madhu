k=input()
a=0
b=["a","e","i","o","u"]
for i in range(0,len(k)-2):
    if k[i] in b and k[i+1] not in b:
        a+=1
        if k[i+1] not in b and k[i+2] in b:
            a+=2
print(b)
