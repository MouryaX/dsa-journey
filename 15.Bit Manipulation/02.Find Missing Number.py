#XOR with a number itself = 0, a^a=0 and a^0=a
#This means the xor of first N natural numbers with xor of all array elements will give Missing Number
arr = [8, 2, 4, 5, 3, 7, 1]
xor1=0
xor2=0
n=len(arr)+1

for i in range(n-1):
    xor1 ^= arr[i]

for i in range(1,n+1):
    xor2 ^= i
    
print(xor1 ^ xor2)
    