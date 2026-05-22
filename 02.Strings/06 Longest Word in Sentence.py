#iterate through string until space and compare curr and max_word
s='I love programming'
curr=''
max_word=''
for ch in s:
    if ch!=' ':
        curr+=ch
    else:
        if len(curr) > len(max_word):
            max_word=curr
        curr=''
if len(curr) > len(max_word):
    max_word=curr
print(max_word)

#Aproach-2 using split and max 
words=s.split()
print(max(words,key=len))