#Find minimum in rotated sorted array
#Approach Rotated sorted array represents two halfs and we will have a break point
#(5 > 1) break point this where sorted order breaks
#if mid > last_ele means min exists in right half so discard left half
#if mid < last_ele means min exists in left half or mid itself is min
nums = [3,4,5,1,2]
l,r=0,len(nums)-1
while l<=r:
    mid=(l+r)//2
    if nums[mid] > nums[r]:
        l=mid+1
    elif nums[mid] < nums[r]:
        r=mid
    else:
        print(nums[r])
        break
#Time:O(log n) Space:O(1)