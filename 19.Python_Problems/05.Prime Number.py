#A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
n=7
c=0
for i in range(1,n+1):
    if n % i == 0:
        c+=1
print(c==2)
#Brute force TLE error may occur beacuse 
#if 1 ≤ n ≤ 109 constrains are given like this

#-----------------------------------------------------------------------------------------------
#Better instead of counting all the factors 
#prime means no divisors exsits except 1 and itslef
#so if you find any divisor rather than two of them return false
f=False
for i in range(2,n):
    if n % i == 0:
        print(False)
        f=True
        break
if not f:
    print(True)
#Still not optimal may get TLE
#Time:O(n) space:O(1)

#--------------------------------------------------------------------------------------------------
#check factors only unitl sqrt(n) why beacuse
#if a number has factors greater than sqrt(n) then that upcoming factors already exist with sqrt(n)
#ex: take 36
#Factor pairs
#1 × 36
#2 × 18
#3 × 12
#4 × 9
#6 × 6
#after sqrt(36)=6 factors repeat 9 x 4 , 12 x 3 ....
#Time:O(sqrt(n)) space:O(1)
#---------------------------------------------------------------------------------------------------
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        print(False)
        f=True
        break
if not f:
    print(True)