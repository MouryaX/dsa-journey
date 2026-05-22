    #We have to find first Non-Repeating char in string and should sort the chars in desc order high freq to low freq
s=input().strip()
freq={}
for x in s:
    freq[x]=freq.get(x,0)+1

#First non-Repeating char means char with freq as 1 and then we have check in original string to preserve order
first_non_rep_char=-1
for ch in s:
    if freq[ch]==1:
        first_non_rep_char=ch
        break
sort_s=sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
res=[]
for ch in sort_s:
    res.extend([ch]*freq[ch])
print("First non repeating char:",first_non_rep_char)
print(res)