#----------------------------------------------------------------------------------------------------
#Print all factors of the given number
#Brute Force
#Time:O(n) space:O(1)
n=36
for i in range(1,n+1):
    if n % i == 0:
        print(i)
#---------------------------------------------------------------------------------------------------

#optimal if you see clearly the factors comes in pairs
#1 × 36
#2 × 18
#3 × 12
#4 × 9
#6 × 6
#so no need of tarversing till n you traverse till sqrt(n)
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        print(i)
        
        if i != n//i:
            print(n//i)
#Time:sqrt(n) space:O(1)

'''
if they said to print in order

if i != n//i:
    large.append(n//i)

for i in reversed(large):
    print(i)'''

