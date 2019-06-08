def fact(k):
    a=1
    for i in range(1,k+1):
        a=a*i
    return a
b,c=map(int,input().split())
print(fact(b)//fact(b-c))
