k,l=map(str,input().split())
a=k|l
b=bin(a)[1:]
print(b.count("1"))
