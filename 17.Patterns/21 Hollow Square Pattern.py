'''
n=5
*****
*   *
*   *
*   *
*****

'''
n=int(input("Enter N: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print("*"*(n))
    else:
        print("*" + " "*(n-2) + "*")