arr=[1, 2, 4, 7, 7, 5] 
first=float('-inf')
second=float('-inf')
for num in arr:
    if num > first:
        second=first
        first=num
    elif num>second and num!=first:
        second=num
print(second)