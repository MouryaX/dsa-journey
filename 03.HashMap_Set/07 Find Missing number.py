#Only possible if array elements are in [1,n] range and dups can be handled but not using formula
arr = [8, 2, 4, 5, 3, 7, 1]
freq={}
for i in range(1,len(arr)+1):
    freq[i]=freq.get(i,0)+1
for num in arr:
    freq[num]=freq.get(num,0)+1
for num in freq.keys():
    if freq[num]==1:
        print(num)
        break

#With formula needed to be in range of [1,n] and must be unqiue or distinct
n=len(arr)+1
ex=n*(n+1)//2
s=sum(arr)
print(ex-s)

