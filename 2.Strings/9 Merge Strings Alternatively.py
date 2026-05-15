#LN:1768
word1 = "abc"
word2 = "pqr"
'''Merged=""
l,r=0,0
while l < len(word1) and r < len(word2):
    Merged+=word1[l]
    Merged+=word2[r]
    l+=1
    r+=1
while l < len(word1):
    Merged+=word1[l]
    l+=1
while r < len(word2):
    Merged+=word2[r]
    r+=1
print(Merged)'''

#Here the Complexity is T:O((m+n)^2) why because each time python copies old string 
#"" + "a"
#"a" + "b"
#"ab" + "c" so many copies complexity increases
#so better to use list+Join 

res = []

l, r = 0, 0
while l < len(word1) and r < len(word2):
    res.append(word1[l])
    res.append(word2[r])
    l += 1
    r += 1
while l < len(word1):
    res.append(word1[l])
    l += 1
while r < len(word2):
    res.append(word2[r])
    r += 1
print("".join(res))

#Traversal:O(m+n) + join():O(m+n) = Total:O(m+n) space:O(m+n    )