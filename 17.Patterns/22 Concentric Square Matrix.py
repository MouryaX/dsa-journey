'''
n=4

    4 4 4 4 4 4 4
    4 3 3 3 3 3 4
    4 3 2 2 2 3 4
    4 3 2 1 2 3 4
    4 3 2 2 2 3 4
    4 3 3 3 3 3 4
    4 4 4 4 4 4 4


'''
n=int(input("Enter N: "))
size=2*n-1
for i in range(size):
    for j in range(size):
        top=i
        left=j
        bottom=size-1-i
        right=size-1-j
        val=n-min(top,left,bottom,right)
        print(val, end=" ")
    print()