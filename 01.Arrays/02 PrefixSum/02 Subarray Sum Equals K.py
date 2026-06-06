#LN:560
#return the total number of subarrays whose sum equals to k
#1 <= nums.length <= 2 * 10^4
#-1000 <= nums[i] <= 1000
#-10^7 <= k <= 10^7
#Sliding window approach fails because it only works on positive numbers but here constraints say nums can also -ve
#Expand means increase shrink means decrease so it fails with -ve numbers
#Brute force
nums = [1,2,3,-3,1,1,1,4,2,-3]
k = 3
n=len(nums)
'''total=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=nums[j]
        if sum == k:
            total += 1
print(total)'''
#Time:O(n^2) for traversal Space:O(1)

#--------------------------------------------------------------------------------------------------------------------
#Optimal using prefixsum and hashmap
#Time:O(n) Space:O(n) prefixsum
freq={}  #Unordered map 
freq[0] = 1 #There may be a subarray exists which is = k and where we can't remove any elements (x-k=0)
prefix, cnt = 0, 0
for i in range(n):
    prefix += nums[i]
    remove_sub = prefix - k
    cnt+=freq.get(remove_sub,0)
    freq[prefix]=freq.get(prefix,0)+1
print(cnt)
#------------------------------------------------------------------------------------------------------