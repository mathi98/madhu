def gcd(a,b):
    if b==0:
        print(a)
    else:
        print(gcd(b,a%b))
a,b=input().split()
GCD=gcd(a,b)
print("",GCD)
