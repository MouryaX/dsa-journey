#First we have find second largest element in array Then We have to print freq of all elements
n=int(input())
arr=list(map(int,input().split()))

#Approach is take two varaibles first=-inf and second=-inf , check element > first then update first and last
#if element > second but != first update second
first=float("-inf")
second=float("-inf")
freq={}

for num in arr:
    freq[num]=freq.get(num,0)+1
    if num>first:
        second=first
        first=num
    elif num > second and num != first:
        second=num
if second==float('-inf'):
    second=-1
print("second:",second)
for k,v in freq.items():
    print(k,"->",v)

     