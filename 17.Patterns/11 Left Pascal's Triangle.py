'''
n=3
*
**
***
**
*
'''
n=int(input("Enter N: "))
for i in range(n):
    print("*"*(i+1))
for i in range(n-2,-1,-1):
    print("*"*(i+1))