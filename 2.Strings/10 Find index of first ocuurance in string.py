#LN:28
#Find the index of first occurance of string needle in haystack and return -1 if not found
haystack = "aaab"
needle = "aab"
n=len(haystack)
m=len(needle)
for i in range(n - m + 1):
    if haystack[i : i + m] == needle:
        print(i)
        break
else:
    print(-1)

#Appraoch First start at each idx and check form each idx to len of needle
#if substring matches return idx else update and check again
#if we use range(n) n=4 it gives 0,1,2,3 but m=3 and if i >= m we can't check substrig idx goes out of range
#ex: if i=3 s1[3:3+3] [3:6] but n onlly ranges till 4 so use n - m + 1
#Time:O((n-m+1)*m) space:O(1)

#Optimal Knuth–Morris–Pratt Algorithm (KMP) Time:O(m+n) space:O(m) for lps array