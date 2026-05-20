#Find the longest length of subarray whose sum <= k
#Brute Force
#Time O(n^2) space:O(1)
k=14
nums=[2,5,1,10,9]
n=len(nums)
max_len=0
'''for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=nums[j]
        if sum <= k:
            max_len=max(max_len,j-i+1)
        if sum > k:
            break
print(max_len)'''

#------------------------------------------------------------------------------------------------------------
#Optimal Sliding window
#Time:O(n) space:O(1)
#Two main operations are there 
#1.Expand +r
#2.shrink -l
#------------------------------------------------------------------------------------------------------------
l,r=0,0
sum=0
while r < n:
    sum+=nums[r]
    while sum > k:
        sum-=nums[l]
        l+=1
    if sum <= k:
        max_len=max(max_len,r-l+1)
    r+=1
print(max_len)