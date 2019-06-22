k=input()
a=[]
for i in range(len(k)):
    if k[i].isdigit():
        a.append(k[i-1]*(int(k[i])-1))
    else:
        a.append(k[i])
print("".join(a))
