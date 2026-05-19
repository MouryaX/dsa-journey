# At the end:
#   all elements before l are smaller
#   all elements after r are bigger
# So:
#   l automatically becomes correct insertion position
nums = [1,3,5,6]
target = 7
l=0
r=len(nums)-1
while l<=r:
    mid=(l+r)//2
    if nums[mid] ==  target:
        print(mid)
        exit()
    elif nums[mid] < target:
        l=mid+1
    else:
        r=mid-1
print(l)
 #Time:O(log n) space:O(1)