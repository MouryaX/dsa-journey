    #LN:69
# Given non-neg x return its sqrt(x) rounded down to the nearest integer
# without any built-in functions and returned int should non-neg
x=4
l,r,ans=0,x,0
while l <= r:
    mid = (l + r) // 2
    sq= mid * mid
    if sq == x:
        print(mid)
        exit()
    elif sq < x:
        ans=mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)
#Time:O(log x) Space:O(1)    
     