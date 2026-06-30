
def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1
    lb = len(nums)

    while start <= end:
        mid = (start+end)//2
        if nums[mid] >= target:
            lb = mid
            end = mid - 1
        else:
            start = mid + 1
    return lb            
        
# ------------------------------------------------------------

nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))

# ------------------------------------------------------------

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))

# ------------------------------------------------------------