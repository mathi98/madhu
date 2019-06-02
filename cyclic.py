import sys,string,math
k,l=map(int,input().split())
l=l%k
a=list(map(int,input().split()))
b=a[-l:]+a[:-l]
print(*b)
