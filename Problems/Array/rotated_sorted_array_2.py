
def search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low+high) // 2

        if nums[mid] == target:
            return True
        
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        
        if nums[mid] <= nums[high]:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return False

# ------------------------------------------------------------

nums = [10, 11, 11, 12, 12, 13, 13, 13, 1, 2, 3, 4]
target = 11
print(search(nums, target))  # Output: True

# ------------------------------------------------------------

nums = [10, 11, 11, 12, 12, 13, 13, 13, 1, 2, 3, 4]
target = 3
print(search(nums, target))  # Output: True

# ------------------------------------------------------------
nums = [10, 11, 11, 12, 12, 13, 13, 13, 1, 2, 3, 4]
target = 8
print(search(nums, target))  # Output: False

# ------------------------------------------------------------