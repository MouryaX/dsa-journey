#LN:3093
#Given two strings WordsContainer and WordsQuery.For each WQ[i] find String in WC:
# ->That has the Longest Common Suffix with WQ[i] 
# ->WQ = "abcdef" WC = ["zzdef", "yycdef", "abcdef"], ans="abcdef" len=6
# ->If there are two or more with same common suffix pick the smallest one
# ->If there are two or more with same smallest length pick the first occured one

wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]
ans = []

for i in range(len(wordsQuery)):
    suffix = wordsQuery[i]
    
    bestSuffix = -1
    bestLength = float('inf')
    bestIndex = -1
    
    for j in range(len(wordsContainer)):
        common = wordsContainer[j]
        l, r = -1, -1
        longestSuffix = 0
        while l >= -len(suffix) and r >= -len(common):
            if suffix[l] == common[r]:
                longestSuffix += 1
            else:
                break
            
            l -= 1
            r -= 1
        
        if longestSuffix > bestSuffix:
            bestSuffix = longestSuffix
            bestLength = len(common)
            bestIndex = j
        elif longestSuffix == bestSuffix:
            if len(common) < bestLength:
                bestLength = len(common)
                bestIndex = j
    ans.append(bestIndex)

print(ans)
         
#Time:𝑂(Q×C×L^2)
    