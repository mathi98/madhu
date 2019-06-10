k=input()
if all(i=="a" or i=="b" for i in k):
    print("yes")
elif all(i=="a" for i in k):
    print("yes")
elif all(i=="b" for i in k):
    print("yes")
else:
    print("no")
