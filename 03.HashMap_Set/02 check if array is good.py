#base[n] = [1, 2, ..., n - 1, n, n] 
# (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once
# plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
#Approach array is good if it is :
#Conditions:
#Numbers from 1 to n must appear at least once
#Number n appears exactly twice
#All other numbers appear exactly once
#Total length = n + 1
from collections import Counter
nums = [3, 4, 4, 1, 2, 1]
freq={}
for x in nums:
    freq[x]=freq.get(x,0)+1  # freq=Counter(nums) Counter automatically store freq of elements in O(n)
n=max(nums)                  #Also counter treats missing element freq as 0 freq[9] == 0 
for i in range(1, n):        #but in normal dict it gives keyError
    if freq.get(i,0) != 1:        #if freq[num] > 1 and num != maxi: here am not checking the missing number
        print(False)        #ANd use freq.get() insetad of direct access freq[i] if i not there error occurs
        exit()
if freq.get(i,0) != 2:
    print(False)
else:
    print(True)

#Time: O(n) build freq + O(n) 1 -> n = O(n)
#Space: O(n)


