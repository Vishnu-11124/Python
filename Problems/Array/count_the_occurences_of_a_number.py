
def firstIndex(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    first = n
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            first = mid
            high = mid - 1
        else:
            low = mid + 1
    return first
            
def lastIndex(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    last = n
    while low <= high:
        mid = (low+high)//2
        if nums[mid] > target:
            last = mid
            high = mid - 1
        else:
            low = mid + 1
    return last

def occurrenceOfANumber(nums, target):
    first = firstIndex(nums, target)
    # print("First Index", first)

    if first == len(nums) or nums[first] != target:
        return 0
    last = lastIndex(nums, target)
    # print("Last Index", last)

    return last - first

# ---------------------------------------------------------------------

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 7, 8, 9, 9, 10]
target = 3
print("Result", occurrenceOfANumber(nums, target))

# ---------------------------------------------------------------------

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 7
print("Result", occurrenceOfANumber(nums, target))

# ---------------------------------------------------------------------
