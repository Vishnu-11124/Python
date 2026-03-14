

def findMissingNumber(array):
    n = len(array)
    
    array_sum = 0

    total_sum = n * (n + 1) // 2

    for i in range(n):
        array_sum += array[i]

    return total_sum - array_sum

# -------------------------------------------------   
         
print(findMissingNumber([0, 1, 2, 4]))  
# Output: 3

# -------------------------------------------------

print(findMissingNumber([0, 1, 2, 3, 4]))  
# Output: 5

# -------------------------------------------------