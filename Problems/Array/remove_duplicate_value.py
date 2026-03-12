
def remove_duplicates(arr):
    j = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    return j + 1, arr


# -------------------------------------------------

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
# Output: 4, [2, 3, 6, 9, 6, 9, 9]

# -------------------------------------------------

print(remove_duplicates([2, 3, 4, 5, 6, 9, 9]))
# Output: 5, [2, 3, 4, 5, 6, 9, 9]

# -------------------------------------------------