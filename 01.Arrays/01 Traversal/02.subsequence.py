def subsequences(i, temp):
    if i == len(arr):
        print(temp)
        return
    
    # take
    temp.append(arr[i])
    subsequences(i + 1, temp)
    
    # not take
    temp.pop()
    subsequences(i + 1, temp)

arr = [1, 2, 3] #array is not passed but can be accessed in function because it becomes global variable 
subsequences(0, [])# but modifying arr inside function will need global keyword