

def right_rotate(array):
    old_value = array[0]
    n= len(array)

    for i in range(0, n-1):
        value = array[i + 1]
        array[i + 1] = old_value
        old_value = value

    array[0] = old_value  

    return array  

# ------------------------------------------------------

print(right_rotate([2, 4, 6, 8, 10]))
# Output: [10, 2, 4, 6, 8]

# ------------------------------------------------------

print(right_rotate([1, 2, 3, 4, 5]))
# Output: [5, 1, 2, 3, 4]

# ------------------------------------------------------

