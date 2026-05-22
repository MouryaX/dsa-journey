#Checking if given two strings are anagrams are not 
#Angrams means same chars with same freq in both strings
#Aproach-1 using sorting complexity:O(nlogn)
s1="Listen".lower()
s2="silent".lower()
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
    
#Aproach-2 using hashmap
freq={}
for ch in s1:
    freq[ch]=freq.get(ch,0)+1
for ch in s2:
    if ch not in freq or freq[ch]==0:
        print("Not Anagram")
        break
    freq[ch]-=1
else:
    print("Anagram")