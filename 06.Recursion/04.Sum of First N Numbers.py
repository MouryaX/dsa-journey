#Functional Recursion
def fun(x):
    if x == 1:
        return 1
    return x + fun(x-1) 

n=5
res = fun(n)
print(res)

#Time: O(N),The function is called N times, with each call performing O(1) work.
#Space: O(N),Due to recursive function calls being stored on the call stack, which grows linearly with N.
