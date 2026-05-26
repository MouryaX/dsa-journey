#LN:3120
#You are given a string word. 
#A letter is called special if it appears both in lowercase and uppercase in word.
word="aaAbCbBc"
seen1 = set(word)
seen2 = set()
cnt=0
for ch in seen1:
    if ch.lower() in seen1 and ch.upper() in seen1:
        if ch.lower() not in seen2:
            cnt+=1
        seen2.add(ch.lower())
            
print(cnt)

#Time:O(n) for set creation + O(1) lookup = O(n) Space:O(n)

#----------------------------------------------------------------------------------------------------
lower=[0] * 26
upper=[0] * 26

for ch in word:
    if ch.islower():
        lower[ord(ch) - ord('a')] = 1
    if ch.isupper():
        upper[ord(ch) - ord('A')] = 1

cnt=0

for i in range(26):
    if  lower[i] and upper[i]:
        cnt+=1
print(cnt)

#Time:O(n) tarversal + O(26) last loop =O(n)
#Space:O(1) beacuse of array with only 26 chars
