'''
n=3

  A
 ABA
ABCBA

'''
n=int(input("Enter N: "))
for i in range(n):
    print(" "*(n-(i+1)),end='')
    for j in range(i+1):
        print(chr(64 + (j+1)),end='')
    for j in range(i,0,-1):
        print(chr(64 + (j)),end='')
    print()