'''
n=10

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

'''
n=int(input("Enter N: "))
half=n//2
for i in range(half):
    print("*"*(i+1) + " "*(n-2*(i+1)) + "*"*(i+1))
for i in range(half-1,0,-1):
    print("*"*(i) + " "*(n-2*i) + "*"*(i))