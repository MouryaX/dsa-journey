nums=[0,0,1,0,0,1]
l,r=0,len(nums)-1
c=0
while l < r:
    if nums[r] == 0: 
        r-=1 
        continue
    if nums[l] == 0:
        nums[l], nums[r] = nums[r], nums[l]
        c+=1
    l+=1
print(c)