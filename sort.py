a=int(input())
list=[int(i) for i in input().split()]
list.sort()
print(*list,sep=" ")
