#----------------------------------------------------------------------------------------------------------
#Constraints:
#1 <= nums.length <= 10^5
#10^4 <= nums[i] <= 10^4
#Optimal approach is using kadane's algorithm for now just traversal
#Approach-1 
nums = [2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
maxx=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=nums[j]
        maxx=max(maxx,sum)
print(maxx)
#Time: O(n^2) Space: O(1)b  

#-----------------------------------------------------------------------------------------------------------
#Approach-2 using prefix sum 
#Build prefix sum first O(n) then compute sum in O(1) usin prefix sum 
#still two loops and complexity remains same
nums = [-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
prefix=[0]*n
prefix[0]=nums[0]

for i in range(1,n):
    prefix[i]=prefix[i-1] + nums[i]

maxx=0
for i in range(n):
    for j in range(i,n):
        if i==0:
            s=prefix[0]
        else:
            s=prefix[j]-prefix[i-1]
        maxx=max(maxx,s)
print(maxx)
 
#Time: O(n) prefix + O(n^2) iteration Space: O(n) for prefix

#------------------------------------------------------------------------------------------------------
#Optimal Sloution using Kadane's Algorithm
#Time:O(n) Space:O(1)
#Approach
#Never carry the sum if its < 0 
max_sum = float('-inf')
sum = sub_start = sub_end = 0
for i in range(n):
    if sum == 0 : start = i
    
    sum += nums[i]           #curr_sum = max(curr_sum + nums[i], nums[i]) but this will carry negative
    
    if sum > max_sum:
        max_sum = sum
        sub_start = start    
        sub_end = i
    
    if sum < 0:
        sum = 0
print(max_sum, nums[sub_start : sub_end + 1])


