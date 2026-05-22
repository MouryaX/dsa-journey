arr = [1, 2, 3, 4]
n=len(arr)
"""subarray n(n+1)//2 
Fix a start indx and expand end indx
idx:0
    [1]
    [1,2]
    [1,2,3]
idx:1
    [2]...."""
for i in range(n):
    temp=[]
    for j in range(i,n):
        temp.append(arr[j])
        print(temp)