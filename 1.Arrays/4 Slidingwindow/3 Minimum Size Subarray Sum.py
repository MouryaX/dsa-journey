#LN:209
# Return the minimal length of a subarray whose sum >= target
target = 7
nums = [2,3,1,2,4,3]
r,n=0,len(nums)
sum,mini=0,float('inf')
for l in range(n):
    while r < n and sum < target:
        sum+=nums[r]
        r+=1
    if sum >= target:
        mini=min(mini,r-l)
    sum-=nums[l]
if mini == float('inf'):
    print(0)
else:
    print(mini)