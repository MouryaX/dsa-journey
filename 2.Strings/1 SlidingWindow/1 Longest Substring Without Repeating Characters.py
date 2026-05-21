1#LN:3
# The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
s = "pwwkew"
maxi=0
for i in range(len(s)):
    seen=set()
    for j in range(i,len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        maxi=max(maxi,j-i+1)
print(maxi)
#Time:O(n^2) space:O(k) k->unqiue chars

#---------------------------------------------------------------------------------------------------------------------
#Optimal Time:O(n) space:O(k) using sliding window or two pointers
seen=set()
l=0
r=0
while r < len(s):
    while s[r] in seen:       #cant keep if because it only checks one char and removes l element but duplicate
                              #May still be in set so until there is no duplicate you should remove elements
        seen.remove(s[l])
        l+=1
    seen.add(s[r])
    maxi=max(maxi,r - l + 1)  #len(seen) may take more time so optimal way is (r - l + 1)
    r+=1
print(maxi)