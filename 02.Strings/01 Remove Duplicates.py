#using ASCII values
s=input().strip()
uniq=""
vis=[0]*256

for ch in s:
    if vis[ord(ch)]==0:
        uniq+=ch
        vis[ord(ch)]=1

print(uniq)
print("Yes" if uniq==uniq[::-1] else "No")

#using dict
uniq="".join(dict.fromkeys(s))