#LN:7
n=12345
n_str=str(n)
rev=[]
for i in range(len(n_str)-1,-1,-1): #str(n)[::-1]
    rev.append(n_str[i])
print(int("".join(rev)))
#Time:O(d) str(n) + O(d) traversal + O(d) int(convertion) = O(d) d->no.of digits
#Space O(d) to store string

#------------------------------------------------------------------------------------
#Approach-2
#Time:O(d) Space:O(1)
#-------------------------------------------------------------------------------------
rev=0
while n > 0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)

#----------------------------------------------------------------------------------------------
#Approach-3 
#leetcode problem 
#Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.
#Time:O(d) d-> no.of digits Space:O(1)
#-------------------------------------------------------------------------------------------------
x = -123
INT_MAX,INT_MIN=2**31-1,-2**31
sign=-1 if x<0 else 1
x=abs(x)
rev=0
while x > 0:
    digit=x%10
    rev=rev*10+digit
    x//=10
rev*=sign
if rev < INT_MIN or rev > INT_MAX:
    print(0)
else:
    print(rev)