
#--------------------------------------------------------------------------------------------------
#Prime number is divisible by only 1 and itself
#Brute force 
#Time:O(n) Space:O(1)
def isPrime(n):
    cnt = 0
    for i in range(1,n + 1):
        if n % i == 0:
            cnt += 1
    return cnt == 2

n = 1483
prime = isPrime(n)
if prime:
    print(n,"Is Prime")
else:
    print(n,"Is Not Prime")
    
#----------------------------------------------------------------------------------------------------

#optimal Time:O(sqrt(n)) Space:O(1)
def isPrime(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            cnt += 1
            
            if n//i != i:
                cnt+=1
    return cnt == 2

n = 1483
prime = isPrime(n)
if prime:
    print(n,"Is Prime")
else:
    print(n,"Is Not Prime")