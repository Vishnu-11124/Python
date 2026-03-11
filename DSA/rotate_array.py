# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# ------------------------------------------------------


class Solution:
    def right_rotate(self, nums, k):
        n = len(nums)
        k = k % n

        nums.reverse()

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        return nums


# ------------------------------------------------------

print(Solution().right_rotate([2, 4, 6, 8, 10], 2))
# Output: [8, 10, 2, 4, 6]

# ------------------------------------------------------

print(Solution().right_rotate([1, 2, 3, 4, 5], 3))
# Output: [3, 4, 5, 1, 2]

# ------------------------------------------------------
