#LN:283
nums = [1,0,3,12]
l,r=0,0
while r < len(nums):
    if nums[r] == 0:
        r+=1
    else:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r+=1
print(nums)
#TIme:O(n) space:O(1)
#stable movement of valid elements