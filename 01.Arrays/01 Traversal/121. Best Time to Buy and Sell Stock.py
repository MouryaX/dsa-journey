#maximize the profit by choosing a single day to buy one stock and sell on another day IN FUTURE
#we can do it in two ways one is simple tarversal and another one two pointers
#Approac-1 Traversal

prices = [7,1,5,3,6,4]
maxx,minn=0,float('inf')
for price in prices:
    minn=min(minn,price)
    maxx=max(maxx,price-minn)
print(maxx)

#pattern iterate through array and find min price first then compute max profit by substracting
#the future price with min

#Apporach-2 Two pointers goto two pointers