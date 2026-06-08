#lambda is short-lived anonymous function used to pass simple logic, it doesn't have any name
a = 'GeeksforGeeks'
upper = lambda x: x.upper()  
print(upper(a))

#List Comprehension + Lambda
func = [lambda arg=x: arg * 10 for x in range(1, 5)] #it stores multiple lambda functions
for i in func:
    print(i())  #i calls the lambda  function func[0],func[1] .... so on and calculated value returned
#value returned automatically no need to type return

#filter(): This function uses a lambda expression to select elements from a list that satisfy a given condition

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))

#If we pass None the it removes all "falsy" values
data = [0, 1, "", "hello", False, True, None]

print(list(filter(None, data)))

#out:[1,"hello",True]

#map() used return map of objects can be converted to list using list()
a = [1, 2, 3, 4]
double = map(lambda x: x * 2, a)
print(list(double))

#reduce() is used to combine all elements of an iterable into a single value.
#Take the first two elements → combine them
#Take the result and the next element → combine again
#Keep going until only one value remains
from functools import reduce
a = [1, 2, 3, 4]
mul = reduce(lambda x, y: x * y, a)
print(mul)