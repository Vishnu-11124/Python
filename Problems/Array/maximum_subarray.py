

def maximumSubarray(array):
    n = len(array)
    maximumValue = float("-inf")
    sum = 0

    # Brute Force Solution
    # for i in range(n):
    #     sum = 0
    #     for j in range(i,n):
    #         sum += array[j]
    #         if sum > maximumValue:
    #             maximumValue = sum

    # Kadane's Algorithm

    for i in range(n):
        sum += array[i]
        maximumValue = max(maximumValue, sum)

        if sum < 0:
            sum = 0

    return maximumValue

# -------------------------------------------------

print(maximumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# -------------------------------------------------

print(maximumSubarray([5, 4, -1, 7, 8]))

# -------------------------------------------------