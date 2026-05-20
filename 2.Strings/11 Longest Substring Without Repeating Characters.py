#LN:3
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

#Optimal Time:O(n) space:O(k) using sliding window or two pointers