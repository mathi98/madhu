k=str(input())
a=""
for i in k:
    if i.isupper():
        a=a+i.lower()
    else:
        a=a+i.upper()
print(a)
