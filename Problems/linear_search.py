
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# -------------------------------------------------

print(linear_search([1, 2, 3, 4, 5], 3))  # Output: 2

# -------------------------------------------------

print(linear_search([10, 20, 30, 40, 50], 60))  # Output: -1

# -------------------------------------------------