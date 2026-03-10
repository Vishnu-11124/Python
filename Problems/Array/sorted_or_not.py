
def array_sorted_or_not(array):
    n =len(array)
    if n == 0 or n == 1:
        return True
    for i in range(0, n-1):
        if array[i] > array[i+1]:
            return False
    return True

# -------------------------------------------------

print(array_sorted_or_not([1, 2, 3, 4, 5]))  # True

# -------------------------------------------------

print(array_sorted_or_not([5, 4, 3, 2, 1]))  # False

# -------------------------------------------------