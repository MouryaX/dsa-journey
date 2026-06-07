nums=[1,3,2,3,1,3,4,3]
k=3
freq={}
for x in nums:
    freq[x]=freq.get(x,0)+1
maxi=max(freq,key=freq.get)

l=0
for num in nums:
    if num != maxi and k > 0:
        k-=1
    elif num != maxi and k == 0:
        print(l)
        exit()
    else:
        l+=1
print(l)