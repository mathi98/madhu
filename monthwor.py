k=list(map(int,input().split("-")))
l=["January","February","March","April","May","June","July","August","September","October","November","December"]
for i in range(len(l)+1):
    if k[1]==i:
        print(l[i-1])
