#Find a contiguous subarray whose length is equal to k that has the maximum average value 
#And return this value. Any answer with a calculation error less than 10-5 will be accepted.
#meaning 10^−5=0.00001
#so allowed error is 0.00001 , ∣your answer−actual answer∣<0.00001 ex:|5.123456 - 5.123460| differnce is 0.000004
nums = [1,12,-5,-6,50,3]
l,k = 0,4
window_sum = sum(nums[:k])
maxi = window_sum / k
for r in range(k,len(nums)):
    window_sum -= nums[l]
    window_sum += nums[r]
    avg_sum = window_sum / k      #Here no need dividing multiple times division is expensive then + - *
    maxi = max(maxi, avg_sum)
    l+=1
print(maxi)

#Instead just calculate max_sum since k is constant a/k > b/k == a > b
#print(maxi / k)
#complexity:O(k) for window sum + O(n-k) for traversal = O(k+(n-k)) = O(n)
#Space:O(1) only variables used no extra space