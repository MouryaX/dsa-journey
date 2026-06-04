def fun(x,n):
    if x == n:
        return
    x += 1
    print(x)     #here if wrote print(x) after fun(x,n) then it prints n to 1 which tail recursion
    fun(x,n)
    
n=5
fun(0,n)

#n to 1 using head
def fun1(x):
    if x == 0:
        return
    print(x)
    fun1(x-1)

N=5
fun1(N)
    
#1 to n using tail
def fun3(x):
    if x == 0:
        return
    fun3(x-1)
    print(x)
n=5
fun3(n)

#n to 1 using tail
def fun4(x,n):
    if x == n+1:
        return
    fun4(x+1,n)
    print(x)
n=5
fun4(n)