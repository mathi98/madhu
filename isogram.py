a=input()
s=a.upper()
for i in a:
    if a.count(i)>1:
        print("No")
        break
    else:
        print("Yes")
