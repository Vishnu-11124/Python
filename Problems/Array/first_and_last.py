def firstIndex(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    first = n

    while low<= high:
        mid = (low+high)//2
        if nums[mid]>=target:
            first = mid
            high =  mid - 1
        else:
            low = mid + 1
    return first 

def lastIndex(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    last = n

    while low<= high:
        mid = (low+high)//2
        if nums[mid]>target:
            last = mid
            high = mid - 1
        else:
            low = mid + 1
    return last          

def searchRange(nums, target):
    first = firstIndex(nums,target)

    if first == len(nums) or nums[first] != target:
        return [-1, -1]


    last = lastIndex(nums,target)
    return [first,last-1] 

# ---------------------------------------------------

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))

# ---------------------------------------------------

nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums, target))

# ---------------------------------------------------
  