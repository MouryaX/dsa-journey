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