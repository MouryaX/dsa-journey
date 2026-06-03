#Array elements can be merged only when: Ai & Aj == 0
#Since disjoint bits cause no carry during addition: Ai + Aj = Ai | Aj
from functools import reduce
from operator import or_

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print("Yes")
        continue

    if sum(a) == reduce(or_, a):
        print("Yes")
    else:
        print("No")