def fun1(): 
    a = 45
    def fun2(): 
        nonlocal a  #non-local tells python to use the outer variable a instead of creating new one
        a=54
        print(a)
    fun2()
    print(a)
fun1()

#Closures in python are memory equipped functions. They allow the function to remember its value even after its excution is completed
# A closure is formed when:
#-->A function is defined inside another function (nested function).
#-->The inner function references variables from the outer function.
#-->The outer function returns the inner function. 

def outer_function(x):
    # Outer function: takes 'x' and defines inner_function
    def inner_function(y):
        return x + y  # 'x' is remembered from outer_function
    return inner_function  # Returns inner function (closure)

# Create a closure with x = 10
closure = outer_function(10)     # Here, x value is remembered by closure variable

# Call the closure with different values of 'y'
print(closure(5)) 
print(closure(20))

#Here we are encapsulating the helper task of cleaning the white spaces
def process_data(data):
    def clean_data():
        return [item.strip() for item in data] 
    return clean_data()
print(process_data(["  Python  ", "  Inner Function  "]))