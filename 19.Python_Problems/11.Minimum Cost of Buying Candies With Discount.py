cost = [6,5,7,9,2,2]
cost.sort(reverse = True)
min_cost = 0
for i in range(len(cost)):
    if (i + 1) % 3 != 0:
        min_cost += cost[i] 
print(min_cost)
#Time: O(n log n) + O(n) = O(n)
#Space: O(1) Auixilary Space but python uses built-in Timsort which may allocate temporary memory
#So in worst case O(n)

#-------------------------------------------------------------------------------------------------------------------------
#1 <= cost.length <= 100
#1 <= cost[i] <= 100
#So the maximum elements can upto 100 
#Time: O(n + 100) = O(n)
#Space: O(100) = O(1)

freq = [0] * 101

for x in cost:
    freq[x] += 1

ans = 0
cnt = 0   # every 3rd candy is free

for price in range(100, 0, -1):

    while freq[price] > 0:

        cnt += 1

        if cnt % 3 != 0:
            ans += price

        freq[price] -= 1

print(ans)