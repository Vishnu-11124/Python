
def moveXerosToEnd(array):
    n = len(array)
    j = 0
    
    for i in range(n):
        if array[i] != 0:
            array[j], array[i] = array[i], array[j]
            j += 1

    return array       

# -------------------------------------------------

print(moveXerosToEnd([0,1,0,3,12]))  
# Output: [1, 3, 12, 0, 0]

# -------------------------------------------------

print(moveXerosToEnd([0,0,0,0,0]))  
# Output: [0, 0, 0, 0, 0]
# All elements are zero, so the output remains the same.

# -------------------------------------------------

print(moveXerosToEnd([1,2,3,4,5]))
# Output: [1, 2, 3, 4, 5]
# No zeros in the array, so the output remains the same.

# -------------------------------------------------         