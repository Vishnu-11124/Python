
def largest_element(array):
    if len(array) == 0:
        return None

    high_index = 0

    for i in range(1, len(array)):
        if array[high_index] < array[i]:
            high_index = i

    return array[high_index]

# -------------------------------------------------

print(largest_element([34, 67, 3, 98, -4]))
# Output: 98

# -------------------------------------------------

print(largest_element([-10, -20, -3, -1, -5]))
# Output: -1

# ------------------------------------------------- 