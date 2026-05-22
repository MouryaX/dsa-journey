'''
n=5

ABCDE                       #A -> 65 , a -> 97
ABCD
ABC
AB
A

'''
n=int(input("Enter N: "))
for i in range(n):
    for j in range(n-i):
        print(chr(64 + (j+1)),end="")
    print()