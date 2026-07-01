
def ceilTheFloor(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    floor = -1
    ceil = -1

    while low <= high:
        mid = (low+high)// 2

        if(nums[mid]== target):
            return [nums[mid], nums[mid]]
        elif nums[mid] < target:
            floor = mid
            low = mid + 1
        else:
            ceil = mid
            high = mid - 1
    return [nums[floor], nums[ceil]]            

# ---------------------------------------------------------

nums = [3,4,4,4,8,9,9,10,12,12,14,15]
print(ceilTheFloor(nums, 8))

# ---------------------------------------------------------

nums = [3,4,4,4,8,9,9,10,12,12,14,15]
print(ceilTheFloor(nums, 11))

# ---------------------------------------------------------

nums = [3,4,4,4,8,9,9,10,12,12,14,15]
print(ceilTheFloor(nums, 16))

# ---------------------------------------------------------
