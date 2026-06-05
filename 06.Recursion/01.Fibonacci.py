#Calculate nth fibonacci number

#Fibonacci is sum of its two pervious numbers
# direct formula:F(n)=F(n−1)+F(n−2)
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))