#Find maximum sum of subarray of size k
nums=[3,5,6,-1,3]
k=4
window_sum=sum(nums[:k])
max_sum=window_sum

l=0
for r in range(k,len(nums)):
    window_sum+=nums[r]
    window_sum-=nums[l]
    max_sum=max(max_sum,window_sum)
    l+=1
    
print(max_sum)

#Time:O(k) window_sum + O(n-k) tarversal = O(k + (n-k)) = O(n)
#space:O(1)