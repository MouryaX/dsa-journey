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
    for j in range(i+1):
        print(chr(64 + (j+1)),end="")
    print()