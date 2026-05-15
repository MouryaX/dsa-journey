#iterate through the array and another iteration for inside array then add each jth bank wealth
accounts = [[1,5],[7,3],[3,5]]
maxx,total=0,0
'''for i in range(len(accounts)):
    wealth=0
    for j in range(len(accounts[i])):
        wealth+=accounts[i][j]'''
for wealth in accounts:
    total=sum(wealth)#even with sum() the complexity remains same sum(2,3) O(1) but sum(arr) O(n)
    
    maxx=max(maxx,total)
    
print(maxx)

#Time: O(m x n) space:O(1)