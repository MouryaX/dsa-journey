arr=[1,2,3,4,5,6,7,8]#sorted array
t=int(input("Enter target: "))
f=False
l,r=0,len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==t:
        print(arr[mid],"Index: ",mid)
        f=True
        break
    elif arr[mid]<t:
        l=mid+1
    else:
        r=mid-1
if not f:
    print("Element not found")
    