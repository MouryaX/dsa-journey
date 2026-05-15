#pivot index is the index where sum all numbers strictly to the left of the index is equal sum all numbers of right of that index
#----------------------------------------------------------------
#Brute force 
#Time:O(n^2)
#Space:O(1)
#----------------------------------------------------------------
'''nums = [1,7,3,6,5,6]
f=False
n=len(nums)
for i in range(n):
    left_sum=sum(nums[:i])
    right_sum=sum(nums[i+1:])
    left_sum = 0
    right_sum = 0
    # left side
    for j in range(i):
        left_sum += nums[j] Here its updating left_sum=left_sum + nums[j] so we need to initilize first

    # right side
    for j in range(i+1, n):
        right_sum += nums[j]
        
    if left_sum == right_sum:
        print(i)
        f=True
        break
if not f:
    print(-1)
    
#------------------------------------------------------------------------------------------
#Approach-2 using prefix sum
#for left_sum=prefix[i-1] if it i!=0 initially left_sum=0
#for right_sum=total-prefix[i] prefix of curr
#--------------------------------------------------------------------------------------------
nums = [2,1,-1]
n=len(nums)
prefix=[0]*n
prefix[0]=nums[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+nums[i]
    
f=False
total_sum=prefix[n-1]
for i in range(n):
    if i==0:
        left_sum=0
    else:
        left_sum=prefix[i-1]
    right_sum=total_sum - prefix[i]
    
    if left_sum == right_sum:
        print(i)
        f=True
        break
if not f:
    print(-1)

#Time: O(n) build prefix + O(n) Traversal = O(n)
#Space:O(n) for storing prefix

#---------------------------------------------------------------------------------------------------
#Approach-3
#optimal approach instead of recalculating left and right sums store total sum
#dyanmically update left_sum and for each index compute right_sum=total-left_sum-current_element
#and compare left and right sum if equal pivot found if not return -1
#Time:O(n)
#Space:O(1)
#---------------------------------------------------------------------------------------------------'''
nums = [2,1,-1]
total=sum(nums)
n=len(nums)
f=False
left_sum=0
for i in range(n):
    right_sum=total-left_sum-nums[i]
    if left_sum == right_sum:
        print(i)
        f=True
        break
    left_sum+=nums[i]
if not f:
    print(-1)
    