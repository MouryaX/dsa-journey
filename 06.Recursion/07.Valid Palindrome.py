def valid(l,r,x):
    if l>=r:
        return True
    if x[l] != x[r]:
        return False
    
    return valid(l+1,r-1,x)
    

s = "A man, a plan, a canal: Panama"
x="".join(ch.lower() for ch in s if ch.isalnum())
print(valid(0,len(x)-1,x))