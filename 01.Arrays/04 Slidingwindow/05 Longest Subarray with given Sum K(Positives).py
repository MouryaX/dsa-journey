#Find the longest subarray whose sum == k 
nums = [-3, 5, 1]
k = 15
l=r=0
s,maxi = 0,0
while r < len(nums):
    s+=nums[r]
    while l<=r and s > k:
        s-=nums[l]
        l+=1
    if s == k:
        maxi=max(maxi,r-l+1)
    r+=1
print(maxi)

