try:
    k=int(input())
    b=list(map(int,input().split()))
    b.sort()
    print(2*(b[-1]+b[-2]))
except ValueError:
    print("invalid")

