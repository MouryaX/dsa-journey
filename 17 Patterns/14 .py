'''
n=5

A                         #A -> 65 , a -> 97
AB
ABC
ABCD
ABCDE

'''
n=int(input("Enter N: "))
for i in range(n):
    for j in range(n-i):
        print(chr(64 + (j+1)),end="")
    print()