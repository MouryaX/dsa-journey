'''
n=5

E                        #A -> 65 , a -> 97
D E
C D E
B C D E
A B C D E   

'''
n=int(input("Enter N: "))
for i in range(n):
    for j in range(i+1,0,-1):
        print(chr(64 + (n-j+1)),end=" ")
    print()