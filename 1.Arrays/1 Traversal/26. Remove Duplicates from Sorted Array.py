#-----------------------------------------------------------------------------------------------------
nums = [0,0,1,1,1,2,2,3,3,4] #we need to change in-place in nums 
new_arr=[]
for num in nums:
    if num not in new_arr:
        new_arr.append(num)
for i in range(len(new_arr)):
    nums[i]=new_arr[i]
    
print(len(new_arr),new_arr)

#Time:O(n) x O(n) for not in new_arr because for array in operator compares each and every element 
#space:O(n)
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Approach-2
#using two pointers why because:
#input array is sorted
#problem is with duplication
#---------------------------------------------------------------------------------------------------
nums = [0,0,1,1,1,2,2,3,3,4]
l,r=0,1
k=1
while r < len(nums):
    while nums[l] == nums[r]: #Here 
        r+=1 #here may r==len(nums)
    l+=1
    nums[l],nums[r]=nums[r],nums[l]#so swapping couses indexoutbound error
    #No need to swap just overwrite elements 
    k+=1
    r+=1
print(nums,k)

#------------------------------------------------------------------------------------------------
#Correct code using single pointer
#Time: O(n) space: O(1) 
#------------------------------------------------------------------------------------------------
nums = [0,0,1,1,1,2,2,3,3,4]
l=0
for r in range(1,len(nums)):
    if nums[l] != nums[r]:
        l+=1
        nums[l]=nums[r]
k=l+1
print(k,nums)