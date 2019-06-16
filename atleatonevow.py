k=input()
a=[]
for i in range(k):
    a.append(input())
if all("a" in i or "e" in i or "i" in i or "o" in i or "u" or "a"):
    print("yes")
else:
    print("no")

