#Given a positive integer n, count the number of digits in n that divide n evenly
#A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
#Constraints: 1<= n <=10**6
#Time:O(d) space:O(1)
n=12
c=0
num=n
f=False
while num > 0:
    digit= num % 10
    if digit > 0 and n % digit == 0:
        print(True)
        f=True
        break
if not f:
    print(False) 