N = 6
k=0
arr = [9, -3, 3, -1, 6, -5]

freq={}
ps,maxi=0,0
for i in range(N):
    ps+=arr[i]
    if ps == k:
        maxi=max(maxi,i+1)
    
    rem=ps-k
    if ps not in freq:
        freq[ps]=i
    if rem in freq:
        maxi=max(maxi,i-freq.get(rem))
print(maxi)
    
#Time:O(n) Tarversal
#Space:O(n) worst case can store upto n elements