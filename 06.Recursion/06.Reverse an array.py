#Functional recurion using two pointers
def rev(l,r,arr):
    if l >= r:
        return 
    arr[l],arr[r]=arr[r],arr[l]
    rev(l+1,r-1,arr)
    #return arr no need to return the arr which is already modified in-place
arr=[8,7,6,5,4,3,2,1]
print(rev(0,len(arr)-1,arr))
print(arr)

#Functional recursion using single index
def rev(arr,i,n):
    if i >= n//2:
        return
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    rev(arr,i+1,n)

arr=[8,7,6,5,4,3,2,1]
print(rev(arr,0,len(arr)))
print(arr)

#Time:O(n//2) = O(n) for both approaches
#Space:O(n//2) = O(n) stack space 