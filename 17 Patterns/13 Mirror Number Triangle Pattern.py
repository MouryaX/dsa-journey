'''
n=4
1      1
12    21
123  321
12344321

'''

n=int(input("Enter N: "))
space=2*n
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print(" "*(space-(2*i+2)),end='')
    for j in range(i+1,0,-1):
        print(j,end='')
    print()
    
#Time:Nx(N+N)=2N^2=O(N^2) Space:O(1)

#--------------------------------------------------------------------------------------------------------------------
n = int(input("Enter N: "))

left_side = ""
for i in range(1, n + 1):
    left_side += str(i)
    spaces = " " * (2 * (n - i))
    right_side = left_side[::-1]  # Reverses the string
    print(left_side + spaces + right_side)
#Time:N traversal * (concatination + slicing + spaces) N =O(N^2) space:O(N) (concatination + slicing + spaces)
#--------------------------------------------------------------------------------------------------------------------
