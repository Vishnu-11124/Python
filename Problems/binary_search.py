def binarySearch(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid

    return -1

# ----------------------------------------------------------

nums = [2, 4, 5, 6, 7, 9, 11, 18, 19]
target = 11
print(binarySearch(nums, target))

# ----------------------------------------------------------
