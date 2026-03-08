
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]      # element to be placed
        j = i - 1

        # Move elements that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# -------------------------------------------------

print(insertion_sort([5, 2, 9, 1, 5, 6]))

# Output: [1, 2, 5, 5, 6, 9]

# -------------------------------------------------

print(insertion_sort([12, 11, 13, 5, 6]))

# Output: [5, 6, 11, 12, 13]

# -------------------------------------------------
