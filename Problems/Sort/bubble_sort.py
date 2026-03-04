
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        is_swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True
        if not is_swapped :
            return arr

# -------------------------------------------------

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# Output: [11, 12, 22, 25, 34, 64, 90]

# -------------------------------------------------

print(bubble_sort([5, 1, 4, 2, 8]))
# Output: [1, 2, 4, 5, 8]

# -------------------------------------------------