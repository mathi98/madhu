k=input()
a=0
for i in range(0,len(k)):
    if int(k[i])%2!=0:
        a=a+int(k[i])
if a%2==0:
    print("E")
else:
    print("O")
