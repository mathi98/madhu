import string
k=input()
k.split()
k=k.replace(" ","")
a=[i for i in k if k.count(i)==1]
b=' '.join(a)
print(b.lower())
