#LN:3121
#A letter c is called special if it appears both in lowercase and uppercase in word,
#and every lowercase occurrence of c appears before the first uppercase occurrence of c.
#Approach:
# ->first store the lower case letters with their index
# ->then store the upper case letters with their first occurance index
# ->then compare the if freq1[lower] < freq2[upper]

word = "cCceDC"
cnt = 0
freq1, freq2 = {}, {}
for x in range(len(word)):
    if word[x].islower():
        freq1[word[x]] =  x
    if word[x].isupper() and word[x] not in freq2:
        freq2[word[x]] = x

for x in freq1:
    if x.upper in freq2 and freq1[x] < freq2[x.upper()]:
        cnt += 1 
print(cnt)

#Time:O(n) tarversal + O(26) traversal in freq1 = O(n)
#Space:O(1) Technically Because we are only storing upto 26 chars because dict contains only unqiue

#-------------------------------------------------------------------------------------------------------------------
#Approach-2 using Arrays instead of dict

lower = [-1] * 26
upper = [-1] * 26 # using -1 because index start with 0

for i, a in enumerate(word):
    if a.islower():
        lower[ord(a) - ord('a')] = i
    else:
        idx = ord(a) - ord('A')
        if upper[idx] == -1:
            upper[idx] = i

cnt = 0
for i in range(26):
    if lower[i] != -1 and upper[i] != -1:
        if lower[i] < upper[i]:
            cnt += 1

print(cnt)

#Time:O(n) tarversal + O(26) = O(n)
#Space:O(1) only 26 letters for both lower and upper arrays


        
