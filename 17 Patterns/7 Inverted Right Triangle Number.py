'''
n=5

12345
1234
123
12
1

'''
n=int(input("Enter N: "))
for i in range(n):
    for j in range(n-i):
        print(j+1,end="")
    print()