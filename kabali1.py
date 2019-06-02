k=int(input())
s="kabali"
s=list(s)
a=0
for i in range(k):
    x=input()
    if len(s)==len(x):
        x=list(x)
        b=0
        for i in range(len(s)):
            if s[i] in x:
                b=b+1
        if b==len(s):
            a=a+1
print(a)
