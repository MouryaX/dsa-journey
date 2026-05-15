Python Basics Notes
🔥 1. Variables
🔷 What is Variable?

A variable stores data.

Think:

variable = container

Example:

name = "Rahul"
age = 20

Here:

name stores string
age stores integer
🔷 Rules

✅ can contain:

letters
numbers
underscore _

❌ cannot start with number

🔷 Examples
x = 10
user_name = "Sam"
marks1 = 95
==================================================
🔥 2. Data Types
🔷 int

Whole numbers.

x = 10
🔷 float

Decimal numbers.

pi = 3.14
🔷 str

Text/string.

name = "Alex"
🔷 bool

True or False.

is_login = True
🔷 list

Stores multiple values.

nums = [1,2,3]
🔷 Check Type
print(type(x))
==================================================
🔥 3. Input / Output
🔷 Output → print()

Displays output.

print("Hello")
🔷 Input → input()

Takes user input.

name = input("Enter name: ")
🔷 Important

input() always returns string.

Example:

age = input()

Even if user enters:

20

Python stores:

"20"

(string)

==================================================
🔥 4. Type Conversion

Convert one datatype to another.

🔷 String → Integer
x = int("5")
🔷 Integer → String
s = str(10)
🔷 Float Conversion
x = float("3.5")
🔷 Common Usage
age = int(input("Enter age: "))
==================================================
🔥 5. Conditions

Used for decision making.

🔷 if

Runs when condition true.

age = 18

if age >= 18:
    print("Adult")
🔷 else

Runs when if is false.

if age >= 18:
    print("Adult")
else:
    print("Minor")
🔷 elif

Checks multiple conditions.

marks = 75

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("C")
🔷 Comparison Operators
Operator	Meaning
==	equal
!=	not equal
>	greater
<	smaller
>=	greater equal
<=	smaller equal
==================================================
🔥 6. Loops

Used for repetition.

🔷 for loop

Used when repetitions known.

for i in range(5):
    print(i)

Output:

0 1 2 3 4
🔷 range()
Code	Meaning
range(5)	0 → 4
range(1,5)	1 → 4
range(1,10,2)	step by 2
🔷 Traversing List
nums = [1,2,3]

for x in nums:
    print(x)
🔷 while loop

Runs until condition false.

i = 0

while i < 5:
    print(i)
    i += 1
🔷 Nested Loop

Loop inside another loop.

for i in range(3):
    for j in range(2):
        print(i,j)
🔷 Complexity Note

Nested loops often become:

O(n
2
)

==================================================
🔥 7. Functions

Functions are reusable blocks of code.

🔷 Function Syntax
def greet():
    print("Hello")

Call function:

greet()
🔷 Parameters

Inputs to function.

def greet(name):
    print("Hello", name)

Call:

greet("Sam")
🔷 Return Statement

Returns value from function.

def add(a,b):
    return a+b

Usage:

ans = add(2,3)
print(ans)
🔷 Difference
print()	return
displays output	sends value back
cannot reuse easily	reusable
==================================================
🔥 IMPORTANT BEGINNER TIPS
🔷 Indentation Matters

Python uses spaces/tabs for blocks.

Correct:

if True:
    print("Hi")

Wrong:

if True:
print("Hi")
🔷 Variable Update
x += 1

means:

x = x + 1
🔷 Infinite Loop Danger
while True:

runs forever unless stopped.

🔥 MOST IMPORTANT

Don’t try to memorize syntax mechanically.

Practice by writing small programs:

palindrome
factorial
fibonacci
prime check
reverse number

That builds real understanding.

=========================================================================================

🔥 Python Data Structures Notes + Practice Problems

These are VERY important for:

DSA
LeetCode
interviews
Flask/backend later
==================================================
🔥 1. LISTS
🔷 What is List?

List stores multiple values in one variable.

nums = [1,2,3,4]

Think:

ordered collection
🔷 Features

✅ ordered
✅ mutable (can change)
✅ allows duplicates

🔷 Indexing
nums = [10,20,30]

print(nums[0])   # 10
print(nums[1])   # 20
🔷 Negative Indexing
print(nums[-1])

Output:

30
🔷 Update Value
nums[1] = 100
🔷 Common Methods
Method	Use
append()	add element
pop()	remove last
remove(x)	remove x
sort()	sort list
reverse()	reverse list
🔷 Example
nums = [1,2]

nums.append(3)

print(nums)

Output:

[1,2,3]
🔷 Traversal
for x in nums:
    print(x)
🔥 Practice Problems

Easy:

Find Numbers with Even Number of Digits
Richest Customer Wealth
Maximum Subarray
==================================================
🔥 2. TUPLES
🔷 What is Tuple?

Tuple is like list but:

❌ cannot change after creation
point = (2,3)
🔷 Features

✅ ordered
✅ immutable
✅ faster than lists

🔷 Access
print(point[0])
🔷 Why Use Tuples?

Used when data should not change.

Example:

coordinates
RGB colors
database records
🔷 Tuple Unpacking
x,y = (10,20)

print(x)
print(y)
🔥 Practice Problems
Transpose Matrix
Shuffle the Array

(Mainly for understanding unpacking/indexing.)

==================================================
🔥 3. SETS
🔷 What is Set?

Stores unique values.

nums = {1,2,3}
🔷 Features

✅ unique elements only
✅ unordered
✅ very fast lookup

🔷 Duplicate Removed Automatically
nums = {1,1,2,2,3}

print(nums)

Output:

{1,2,3}
🔷 Add Element
nums.add(5)
🔷 Remove Element
nums.remove(2)
🔷 Fast Lookup
if 3 in nums:

Average complexity:
O(1)

🔥 When To Use Set?

Use when:

checking duplicates
fast searching
uniqueness needed
🔥 Practice Problems
Contains Duplicate
Intersection of Two Arrays
Happy Number
==================================================
🔥 4. DICTIONARIES (HASHMAP)

VERY IMPORTANT FOR DSA.

🔷 What is Dictionary?

Stores:

key → value

pairs.

student = {
    "name":"Rahul",
    "age":20
}
🔷 Access
print(student["name"])
🔷 Add/Update
student["marks"] = 95
🔷 Frequency Count Pattern

VERY IMPORTANT.

freq = {}

for x in nums:
    freq[x] = freq.get(x,0) + 1
🔷 Why get()?
freq.get(x,0)

means:

if x exists → give value
otherwise → return 0
🔷 Lookup Complexity

Average:
O(1)

🔥 Practice Problems
Two Sum
First Unique Character in a String
Valid Anagram
==================================================
🔥 5. STRINGS
🔷 What is String?

Collection of characters.

name = "python"
🔷 Indexing
print(name[0])

Output:

p
🔷 Immutable

Cannot directly modify.

❌

name[0] = 'j'

Error.

🔷 Traversal
for ch in name:
    print(ch)
🔷 Common Methods
Method	Use
lower()	lowercase
upper()	uppercase
strip()	remove spaces
split()	split string
replace()	replace text
isalnum()	alpha numeric check
🔥 Practice Problems
Reverse String
Valid Palindrome
Length of Last Word
==================================================
🔥 6. SLICING
🔷 Syntax
arr[start:end:step]
🔷 Examples
nums = [1,2,3,4,5]

print(nums[1:4])

Output:

[2,3,4]
🔷 Reverse
nums[::-1]
🔷 Important

End index excluded.

nums[1:4]

takes:

1,2,3

NOT 4.

🔥 Complexity

Slicing creates new list/string.

Usually:
O(n)

🔥 Practice Problems
Reverse String
Merge Strings Alternately
==================================================
🔥 7. TRAVERSAL

MOST IMPORTANT DSA FOUNDATION.

🔷 What is Traversal?

Visiting every element one by one.

🔷 Array Traversal
for x in nums:
    print(x)
🔷 Index Traversal
for i in range(len(nums)):
    print(nums[i])
🔷 String Traversal
for ch in s:
    print(ch)
🔥 What You Usually Track
max
min
sum
count
frequency
🔥 Practice Problems
Best Time to Buy and Sell Stock
Find Pivot Index
Running Sum of 1d Array
==================================================
🔥 8. IMPORTANT PYTHON METHODS FOR DSA
🔷 len()
len(nums)
🔷 sum()
sum(nums)

Complexity:
O(n)

🔷 max()
max(nums)
🔷 min()
min(nums)
🔷 sorted()

Returns new sorted list.

sorted(nums)

Complexity:
O(nlogn)

🔷 sort()

Sorts original list.

nums.sort()
🔷 enumerate()

Gives:

index + value
for i,x in enumerate(nums):
🔷 zip()

Combines multiple iterables.

zip(a,b)

Used in:

longest common prefix
matrix problems
🔥 BEST PRACTICE STRATEGY

For every topic:

Learn concept
Write small examples
Solve 2–3 easy LeetCode problems
Revise next day WITHOUT notes

That’s how concepts stick long-term.