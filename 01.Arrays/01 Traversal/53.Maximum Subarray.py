#Constraints:
#1 <= nums.length <= 105
#104 <= nums[i] <= 104
#Optimal approach is using kadane's algorithm for now just traversal
#Approach-1 
nums = [-2,1,-3,4,-1,2,1,-5,4]
maxx=0
for i in range(len(nums)):
    sum=0
    for j in range(i,len(nums)):
        sum+=nums[j]
        maxx=max(maxx,sum)
print(maxx)

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