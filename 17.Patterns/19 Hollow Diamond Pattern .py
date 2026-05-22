'''
n=10
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

'''
n=int(input("Enter N: "))
half=n//2
for i in range(half):
    print("*"*((half)-i) + " "*(2*i) + "*"*((half)-i))
for i in range(half-1,-1,-1):
    print("*"*((half)-i) + " "*(2*i) + "*"*((half)-i))