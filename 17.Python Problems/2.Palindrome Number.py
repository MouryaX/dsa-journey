#LN:9
#Print true if number reads same from left -> right and right->left
x = 123
num=x # store the number beacuse after digit extracation x becomes 0
if x<0:
    print(False)
rev=0
while x > 0:
    digit=x%10
    rev=rev*10+digit
    x//=10
if rev==num:
    print(True)
else:
    print(False)