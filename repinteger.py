k=int(input())
a=bin(k)[2::]
b=a[::-1]
print(b.index("1")+1)
