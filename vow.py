k=input()
vowel=set('aeiou')
if not vowel.isdisjoint(k):
    print("yes")
else:
    print("no")
