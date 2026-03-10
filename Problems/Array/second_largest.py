
def second_largest(array):
    n = len(array)

    if n < 2:
        return "Invalid array"

    if array[0] > array[1]:
        first_val, second_val = 0, 1
    else:
        first_val, second_val = 1, 0

    for i in range(2, n):
        if array[i] > array[first_val]:
            second_val = first_val
            first_val = i
        elif array[i] > array[second_val] and array[i] != array[first_val]:
            second_val = i

    return array[second_val]

# -------------------------------------------------

print(second_largest([55, 32, -97, 99, 3, 67]))
# Output: 67

# -------------------------------------------------

print(second_largest([10, 10, 9, 8, 7]))
# Output: 9

# -------------------------------------------------