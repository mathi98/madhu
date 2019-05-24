k=input()
a=0
b=0
for c in k:
    if(c.isalpha()):
        a=a+1
    elif(c.isnumeric()):
        b=b+1
if(a>0 and b>0):
    print("yes")
else:
    print("no")
