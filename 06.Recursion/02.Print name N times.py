def fun(n):      #here we thought the global var n is modified but the argument var is also n
                #python treats n as local
    if n == 0:
        return
    n -= 1
    print("Mourya")
    fun(n)
    
n=5
fun(n)

#Approach-2
def fun1(i,n):
    if i == n:
        return
    print("Mourya")
    fun1(i+1,n)
n=5
fun1(0,n)