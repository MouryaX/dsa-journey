#two approaches manual and using zip()
#1 manual
strs = ["flower","flow","flight"]
prefix=""
f=True
for i in range(len(strs[0])):
    ch=strs[0][i]
    for w in strs:
        if i>=len(w) or w[i]!=ch:
            f=False
            break
    if not f:
        break
    prefix+=ch

print(prefix)

#T:O(n),S:O(1)

"""2nd using zip() 
zip() groups same index characters ('f','f','f')
('l','l','l')
('o','o','i')
..."""
for ch in zip(*strs):
    if len(set(ch))==1:
        prefix+=ch
    else:
        break
print(prefix)
#T:O(n),S:O(n) for set