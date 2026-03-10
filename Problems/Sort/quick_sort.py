
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)

# -------------------------------------------------

print(quick_sort([5,3,8,4,2,7,1]))
# Output: [1, 2, 3, 4, 5, 7, 8]

# -------------------------------------------------

print(quick_sort([10, 7, 8, 9, 1, 5]))
# Output: [1, 5, 7, 8, 9, 10]

# -------------------------------------------------