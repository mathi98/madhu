k=input()
a=''
for i in k:
    if i=="X":
        a+="A"
    elif i=="Y":
        a+="B"
    elif i=="Z":
        a+="C"
    else:
        a+=chr(ord(i)+3)
print(a)
