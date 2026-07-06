
def findMin(nums):
    n = len(nums)
    low = 0
    high = n - 1
    min_val = float('inf')

    if nums[low] <= nums[high]:
        return min(min_val, nums[low])
    
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] <= nums[high]:
            min_val = min(min_val, nums[mid])
            high = mid - 1
        else:
            min_val = min(min_val, nums[low])
            low = mid + 1
    return min_val

# ------------------------------------------------------------ 

nums = [3,4,5,1,2]
print(findMin(nums))

# ------------------------------------------------------------ 

nums = [4,5,6,7,0,1,2]
print(findMin(nums))

# ------------------------------------------------------------ 

nums = [11,13,15,17]
print(findMin(nums))

# ------------------------------------------------------------ 