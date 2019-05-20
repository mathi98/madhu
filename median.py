def median(list):
    n=len(list)
    if(n<1):
        return None
    elif(n%2==1):
        return sorted(list)[n//2]
    else:
        return sum(sorted(list)[n//2-1:n//2+1])/2.0
