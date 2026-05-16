arr=[1,3,2,4,5,6,7,8]
f=False
t=int(input("Enter target: "))
for i in range(len(arr)):
    if arr[i]==t:
        print(arr[i],"index:",i)
        f=True
        break
if not f:
    print("Element not found")
