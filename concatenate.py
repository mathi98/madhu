k,l=input().split()
if len(k)==len(l):
    print(k+l)
elif len(k)==len(l):
    m=k[:len(l)]+l
    print(m)
else:
    m=k+l[:len(k)]
    print(m)
