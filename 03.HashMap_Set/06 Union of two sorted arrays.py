#Union means combining multiple elements from data collections which are common
#into distinct collection so union = common and unique
#Union without set
arr1=[1,2,3,4,5] 
arr2=[2,3,4,4,5]

freq={}

for num in arr1:
    freq[num]=freq.get(num,0)+1
for num in arr2:
    freq[num]=freq.get(num,0)+1
print(sorted(freq.keys()))

#Using set
s=set(arr1) | set(arr2)
print(s)