arr=[8,7,6,5,4,3,2,1]
n=len(arr)
l,r=0,n-1
while l < r:
    arr[l],arr[r] = arr[r],arr[l]
    l+=1
    r-=1
print(arr)