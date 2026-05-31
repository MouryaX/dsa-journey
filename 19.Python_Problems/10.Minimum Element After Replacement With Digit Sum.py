def min_element(nums):
    digit = 0
    mini = float("inf")
    for num in nums:
        s = 0
        while num > 0:
            digit = num % 10
            s += digit
            num //= 10
                
        if s < mini:
            mini = s

    return mini

nums = [10,12,13,14]
res = min_element(nums)
print(res)