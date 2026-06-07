from collections import Counter,defaultdict
li=[2,3,3,4,5,6,6,7]
freq1=Counter(li) #Used to automatically store frequenices
#Time:O(n)

freq2=defaultdict(list)
for i,num in enumerate(li):
    freq2[num].append(i)

#Accessing elements in defaultdict
print(freq2.keys())
for i in (freq2.keys()):
    print(freq2[i])
print(freq1,freq2) #Used to store positions of element appread as list
#Time:O(n)

