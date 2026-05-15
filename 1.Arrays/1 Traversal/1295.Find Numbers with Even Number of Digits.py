#Dont use % operator for digits it just gives reminder use // int divisor to count digits
nums = [555,901,482,1771]
c=0
for num in nums:
    digits=0
    while num > 0:
        num//=10
        digits+=1
    if digits % 2 == 0:
        c+=1
print(c)

#Time: O(n x d) d-> no.of digits in number ~  log n
#space:O(1)