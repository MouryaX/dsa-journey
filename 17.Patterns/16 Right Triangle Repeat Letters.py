'''
n=5

A                         #A -> 65 , a -> 97
BB
CCC
DDDD
EEEEE

'''
n=int(input("Enter N: "))
for i in range(n):
    print(chr(64 + (i+1))*(i+1))