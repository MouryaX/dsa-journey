#each number is sum of previous two numbers
#starts with 0, 1 
#0 + 1 = 1
#1 + 1 = 2
#1 + 2 = 3
#2 + 3 = 5
n=7
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

#Go to Recursion
