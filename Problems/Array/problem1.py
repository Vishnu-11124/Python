
# Swap array using two pointer

def swap_array( array ):
    left = 0
    right = len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array   

# ------------------------------------------------------

arratOne = [1,2,3,4,5,6]
print(swap_array(arratOne))

# ------------------------------------------------------

arrayName = ["harry", "ravi", "jeena", "john", "virat"]
print(swap_array(arrayName))

# ------------------------------------------------------