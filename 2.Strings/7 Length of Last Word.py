s= "   fly me   to   the moon  "
r,c=len(s)-1,0

while r>=0 and s[r]==" ":
    r-=1

while r>=0 and s[r]!=" ":
    c+=1
    r-=1
    
print(c)