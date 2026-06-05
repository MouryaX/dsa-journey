def rev(l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1


arr = [1,2,3,4,5,6,7]
k = 3
n=len(arr)
k%=n
rev(0,n-1)
rev(0,k-1)
rev(k,n-1)
print(arr)

#Time:O(n) reverse once + O(k) + O(n-k) = O(n)
#Space:O(1) in-place swapping

#Approacch-2
arr = [1,2,3,4,5,6,7]
k = 3
n = len(arr)

temp = [0] * n

for i in range(n):
    temp[(i + k) % n] = arr[i]

arr = temp

#Space:O(n) extra array