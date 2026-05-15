#Approach-2 use two pointers left(buy) , right(sell) 
#check each time if left < right left(buy) should be always less than right then compute profit
#if left > right then update left pointer to right and increment right+=1
'''prices = [7,6,4,3,1]
l,r=0,1
maxx,profit=0,0
while r < len(prices):
    if prices[l] < prices[r]:
        profit=prices[r]-prices[l]
    else:
        l=r
    r+=1
    maxx=max(maxx,profits)
print(maxx)'''''

#improvements no need of extra varibale profit and max is computing each time which is uncessary

prices = [7,6,4,3,1]
l,r=0,1
maxx=0
while r < len(prices):
    if prices[l] < prices[r]:
        profit=prices[r]-prices[l]
        maxx=max(maxx,profits)
    else:
        l=r
    r+=1
print(maxx)

#profit and max is computed only when needed same improvement can improve slight complexity and beats
#Time:O(n) Space:O(1)