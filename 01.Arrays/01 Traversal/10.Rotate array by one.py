nums = [1, 2, 3, 4, 5] 
temp=nums[0]
for i in range(1,len(nums)):
    nums[i-1]=nums[i]
nums[-1]=temp
print(nums)