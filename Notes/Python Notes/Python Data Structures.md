# Python Data Structures — Complete Beginner Notes

---

# 1. LISTS

# 🔥 What is a List?

A list is an ordered, mutable collection of elements.

Think:

```text
List = container that stores multiple values in order
```

Example:

```python
nums = [1,2,3,4]
```

---

# 🔷 Features of Lists

| Feature           | Meaning                              |
| ----------------- | ------------------------------------ |
| Ordered           | Maintains insertion order            |
| Mutable           | Can modify elements                  |
| Allows duplicates | Same value can appear multiple times |
| Indexed           | Access using positions               |
| Dynamic size      | Can grow/shrink                      |

---

# 🔷 Indexing

```python
nums = [10,20,30,40]

print(nums[0])
print(nums[2])
```

Output:

```python
10
30
```

---

# 🔷 Negative Indexing

```python
print(nums[-1])
print(nums[-2])
```

Output:

```python
40
30
```

Meaning:

```text
-1 -> last element
-2 -> second last
```

---

# 🔷 Traversal

```python
for x in nums:
    print(x)
```

---

# 🔷 Updating Values

```python
nums[1] = 100
```

---

# 🔷 List Methods

---

## append()

Adds element at end.

```python
nums.append(5)
```

---

## insert(index,value)

Insert at specific position.

```python
nums.insert(1,50)
```

---

## pop()

Removes last element.

```python
nums.pop()
```

Can also remove by index.

```python
nums.pop(2)
```

---

## remove(value)

Removes first occurrence.

```python
nums.remove(50)
```

---

## sort()

Sorts original list.

```python
nums.sort()
```

Descending:

```python
nums.sort(reverse=True)
```

Complexity:

```text
O(n log n)
```

---

## reverse()

Reverses list.

```python
nums.reverse()
```

---

## index(value)

Returns first index.

```python
nums.index(20)
```

---

## count(value)

Counts occurrences.

```python
nums.count(10)
```

---

## extend()

Adds multiple elements.

```python
nums.extend([7,8,9])
```

---

## clear()

Removes all elements.

```python
nums.clear()
```

---

# 🔷 Special Operators

---

## in

Checks membership.

```python
10 in nums
```

Complexity:

```text
O(n)
```

---

## +

Concatenate lists.

```python
a = [1,2]
b = [3,4]

print(a+b)
```

---

## *

Repeats list.

```python
[0] * 5
```

---

# 🔷 Slicing

```python
nums[1:4]
nums[::-1]
```

---

# 🔥 Final Comprehensive List Code

```python
nums = [4,2,7,2]

# append
nums.append(10)

# insert
nums.insert(1,99)

# extend
nums.extend([8,9])

# remove
nums.remove(2)

# pop
nums.pop()

# count
print(nums.count(2))

# index
print(nums.index(7))

# traversal
for x in nums:
    print(x)

# membership
print(7 in nums)

# sorting
nums.sort()
print(nums)

# reverse
nums.reverse()
print(nums)

# slicing
print(nums[1:4])
print(nums[::-1])

# concatenation
print(nums + [100,200])

# repetition
print([0] * 5)
```

---

---

# 2. TUPLES

# 🔥 What is Tuple?

Tuple is ordered but immutable collection.

```python
point = (10,20)
```

---

# 🔷 Features

| Feature           | Meaning       |
| ----------------- | ------------- |
| Ordered           | Keeps order   |
| Immutable         | Cannot modify |
| Allows duplicates | Yes           |
| Indexed           | Yes           |
| Faster than list  | Slightly      |

---

# 🔷 Accessing

```python
print(point[0])
```

---

# 🔷 Tuple Packing

```python
t = 1,2,3
```

---

# 🔷 Tuple Unpacking

```python
x,y = (10,20)
```

---

# 🔷 Methods

Only two important methods.

---

## count()

```python
t = (1,2,2,3)
print(t.count(2))
```

---

## index()

```python
print(t.index(3))
```

---

# 🔷 Operators

---

## in

```python
2 in t
```

Complexity:

```text
O(n)
```

---

## +

```python
(1,2) + (3,4)
```

---

## *

```python
(1,2) * 3
```

---

# 🔥 Final Comprehensive Tuple Code

```python
t = (1,2,2,3,4)

# indexing
print(t[0])
print(t[-1])

# traversal
for x in t:
    print(x)

# count
print(t.count(2))

# index
print(t.index(3))

# membership
print(4 in t)

# concatenation
print(t + (5,6))

# repetition
print((1,2) * 3)

# unpacking
x,y = (10,20)
print(x,y)
```

---

---

# 3. SETS

# 🔥 What is Set?

Set stores unique unordered values.

```python
s = {1,2,3}
```

---

# 🔷 Features

| Feature       | Meaning         |
| ------------- | --------------- |
| Unordered     | No fixed order  |
| No duplicates | Unique only     |
| Mutable       | Can add/remove  |
| Fast lookup   | Uses hashing    |
| No indexing   | Cannot use s[0] |

---

# 🔷 Duplicate Removal

```python
s = {1,1,2,2,3}
print(s)
```

Output:

```python
{1,2,3}
```

---

# 🔷 Methods

---

## add()

```python
s.add(10)
```

---

## remove()

Removes element.

```python
s.remove(2)
```

Error if absent.

---

## discard()

Safer remove.

```python
s.discard(20)
```

No error.

---

## pop()

Removes random element.

```python
s.pop()
```

---

## clear()

```python
s.clear()
```

---

# 🔷 Set Operations

---

## union()

All elements.

```python
a.union(b)
```

OR:

```python
a | b
```

---

## intersection()

Common elements.

```python
a.intersection(b)
```

OR:

```python
a & b
```

---

## difference()

Elements only in first set.

```python
a - b
```

---

## symmetric_difference()

Not common elements.

```python
a ^ b
```

---

# 🔷 Membership

```python
5 in s
```

Average complexity:

```text
O(1)
```

---

# 🔥 Final Comprehensive Set Code

```python
s = {1,2,3,4}

# add
s.add(10)

# remove
s.remove(2)

# discard
s.discard(100)

# traversal
for x in s:
    print(x)

# membership
print(3 in s)

# set operations
A = {1,2,3}
B = {3,4,5}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)

# pop
s.pop()

print(s)
```

---

---

# 4. DICTIONARIES

# 🔥 What is Dictionary?

Dictionary stores key-value pairs.

```python
student = {
    "name":"Rahul",
    "age":20
}
```

---

# 🔷 Features

| Feature         | Meaning                                                             |
| --------------- | ------------------------------------------------------------------- |
| Key-value pairs | Mapping                                                             |
| Fast lookup     | Hashing                                                             |
| Mutable         | Can modify                                                          |
| Unique keys     | Duplicate keys not allowed                                          |
| Unordered       | Modern Python preserves insertion order but conceptually hash-based |

---

# 🔷 Accessing Values

```python
print(student["name"])
```

---

# 🔷 Adding/Updating

```python
student["marks"] = 95
```

---

# 🔷 Methods

---

## get()

Safer access.

```python
student.get("name")
```

Default value:

```python
student.get("city","Not Found")
```

---

## keys()

```python
student.keys()
```

---

## values()

```python
student.values()
```

---

## items()

Returns key-value pairs.

```python
student.items()
```

---

## pop()

```python
student.pop("age")
```

---

## update()

```python
student.update({"city":"Delhi"})
```

---

## clear()

```python
student.clear()
```

---

# 🔷 Traversal

```python
for k,v in student.items():
    print(k,v)
```

---

# 🔷 Membership

Checks keys.

```python
"name" in student
```

Average complexity:

```text
O(1)
```

---

# 🔥 Frequency Count Pattern

VERY IMPORTANT FOR DSA.

```python
freq = {}

for x in nums:
    freq[x] = freq.get(x,0) + 1
```

---

# 🔥 Final Comprehensive Dictionary Code

```python
student = {
    "name":"Rahul",
    "age":20
}

# access
print(student["name"])

# get
print(student.get("city","Not Found"))

# add/update
student["marks"] = 95

# update
student.update({"city":"Hyderabad"})

# traversal
for k,v in student.items():
    print(k,v)

# keys
print(student.keys())

# values
print(student.values())

# membership
print("name" in student)

# pop
student.pop("age")

print(student)

# frequency count
nums = [1,1,2,3,2,1]

freq = {}

for x in nums:
    freq[x] = freq.get(x,0) + 1

print(freq)
```

---

---

# 5. STRINGS

# 🔥 What is String?

String is sequence of characters.

```python
s = "python"
```

---

# 🔷 Features

| Feature   | Meaning                   |
| --------- | ------------------------- |
| Ordered   | Characters maintain order |
| Immutable | Cannot modify directly    |
| Indexed   | Access by position        |
| Iterable  | Traversable               |

---

# 🔷 Indexing

```python
print(s[0])
print(s[-1])
```

---

# 🔷 Traversal

```python
for ch in s:
    print(ch)
```

---

# 🔷 Slicing

```python
print(s[1:4])
print(s[::-1])
```

---

# 🔷 String Methods

---

## lower()

```python
s.lower()
```

---

## upper()

```python
s.upper()
```

---

## strip()

Removes spaces.

```python
"  hi  ".strip()
```

---

## split()

Splits into list.

```python
"a b c".split()
```

---

## replace()

```python
s.replace("p","j")
```

---

## find()

Returns index.

```python
s.find("t")
```

---

## count()

```python
s.count("o")
```

---

## startswith()

```python
s.startswith("py")
```

---

## endswith()

```python
s.endswith("on")
```

---

## isdigit()

```python
"123".isdigit()
```

---

## isalpha()

```python
"abc".isalpha()
```

---

## isalnum()

```python
"abc123".isalnum()
```

---

# 🔷 Operators

---

## +

Concatenation.

```python
"hello" + "world"
```

---

## *

Repetition.

```python
"ha" * 3
```

---

## in

Membership.

```python
"py" in s
```

Complexity:

```text
O(n)
```

---

# 🔥 Final Comprehensive String Code

```python
s = " Python Programming "

# strip
s = s.strip()

# lower
print(s.lower())

# upper
print(s.upper())

# indexing
print(s[0])
print(s[-1])

# traversal
for ch in s:
    print(ch)

# slicing
print(s[0:6])
print(s[::-1])

# split
words = s.split()
print(words)

# replace
print(s.replace("Python","Java"))

# find
print(s.find("Program"))

# count
print(s.count("m"))

# startswith
print(s.startswith("Python"))

# endswith
print(s.endswith("ing"))

# membership
print("thon" in s)

# repetition
print("ha" * 3)

# checks
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
```

---

# 🔥 MOST IMPORTANT DSA TAKEAWAYS

| Data Structure | Best Use                  |
| -------------- | ------------------------- |
| List           | Traversal, indexing       |
| Tuple          | Fixed immutable data      |
| Set            | Fast lookup, duplicates   |
| Dictionary     | Frequency count, mappings |
| String         | Character manipulation    |

---

# 🔥 IMPORTANT COMPLEXITIES

| Operation | List        | Set      | Dictionary |
| --------- | ----------- | -------- | ---------- |
| Lookup    | O(n)        | O(1) avg | O(1) avg   |
| Insert    | O(1) append | O(1) avg | O(1) avg   |
| Delete    | O(n)        | O(1) avg | O(1) avg   |
| Indexing  | O(1)        | ❌        | key-based  |
