#An Armstrong number is a number such that the sum of the cubes of its digits
# is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371.
#A number whose sum of each digit raised 
#to the power of total number of digits 
#is equal to the number itself.
n = 9474
power=len(str(n))
num=n
arm=0
while num > 0:
    arm+=(num % 10)**power
    num//=10
print(arm==n)
#Time:O(d) str() + O(d) digit extraction = O(d) Space:O(d) for power storing