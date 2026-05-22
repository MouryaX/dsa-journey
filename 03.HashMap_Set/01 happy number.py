#LN:202
#Happy number means: do sum of square of digits if it == 1 then happy number
#If number repeats cycle detected 
#Approach its linked with duplication meaning hash set to see repeated number
#calculate sum of squares of digit iteratively until == 1 or same number repeats
n=19
seen=set()
while n!=1 and n not in seen:
    seen.add(n)
    total=0
    while n>0:
        digit=n%10
        total+=digit**2  #n=sum(int(digit)**2 for digit in str(n))
        n//=10
    n=total
print(n==1)