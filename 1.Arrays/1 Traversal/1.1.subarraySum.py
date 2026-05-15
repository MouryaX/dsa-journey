arr = [1, 2, 3, 4]
n=len(arr)
#prefix sum
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        print(sum)