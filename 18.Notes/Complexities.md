🔥 Techniques for O(n)
Technique	Complexity
Linear traversal	O(n)
Sliding window	O(n)
Two pointers	O(n)
Prefix sum	O(n)
HashMap	O(n)
Stack	O(n)
Queue	O(n)
🔥 Techniques for O(n log n)
Technique	Complexity
Sorting	O(n log n)
Binary Search	O(log n)
Heap/Priority Queue	O(log n) per operation
Merge Sort	O(n log n)
🔷 Example

If:

n ≤ 10^5

Then:
❌ O(n²) → too slow

Because:

10
10

operations.

Impossible.

🔥 So your brain should think:

For:

n ≤ 10^5

Use:
✅ sliding window
✅ hashing
✅ binary search
✅ sorting
✅ greedy

🔷 n ≤ 10⁶

Only:

✅ O(n)

is usually safe.

🔥 Common O(n) Techniques
Technique	Use
Prefix sum	range sums
Sliding window	subarray/window
Hashing	fast lookup
Greedy	optimal local decisions
Stack	monotonic problems
🔷 n ≥ 10⁷

Need extremely fast.

Usually:

O(log n)
O(1)

only.

==================================================
🔥 MOST IMPORTANT INTERVIEW PATTERN MAPPING
🔷 If complexity should be O(n)

Think:

Problem Type	Technique
Subarray/window	Sliding window
Range sum	Prefix sum
Fast lookup	HashMap
Pair from ends	Two pointers
Next greater	Stack
🔷 If complexity should be O(log n)

Think:

Situation	Technique
Sorted array	Binary search
Search space reduction	Binary search
Repeated ordered operations	Heap
🔷 If complexity should be O(n log n)

Think:

Situation	Technique
Sorting needed	Sort
Ordered processing	Heap
Divide & conquer	Merge sort
🔥 MASTER SHORTCUT (VERY IMPORTANT)
Complexity	Typical Techniques
O(n)	Sliding window, hashing, two pointers
O(log n)	Binary search
O(n log n)	Sorting + binary search
O(n²)	Nested loops
O(2ⁿ)	Recursion/backtracking