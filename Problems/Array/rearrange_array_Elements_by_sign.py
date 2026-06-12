# def rearrangeArray(nums):
#     if(len(nums) % 2 != 0):
#         return "Invalid array length"

#     if( len(nums) <= 2 or len(nums) >= 2*(10**5)):
#         return "Invalid array length"

#     positive = []
#     negative = []

#     for i in nums:
#         if i < 0:
#             negative.append(i)
#         else:
#             positive.append(i)


#     if(len(positive) != len(negative)):
#         return "Invalid array"

#     result = []

#     for i in range(len(positive)):
#         result.append(positive[i])
#         result.append(negative[i])

#     return result


def rearrangeArray(nums):
    n = len(nums)
    result = [0] * n
    posInd, negInd = 0, 1
    for i in range(n):
        if nums[i] >= 0:
            result[posInd] = nums[i]
            posInd += 2

        else:
            result[negInd] = nums[i]
            negInd += 2
    return result


# -------------------------------------------------

resultarray = rearrangeArray([3, 1, -2, -5, 2, -4])
print("Result Value:", resultarray)
