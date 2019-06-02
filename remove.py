k=int(input())
a=input()
b=''
for i in range(-1,-k-1,-1):
    if a[i].lower() not in "aeiou":
        b+=a[i]
print(b)
