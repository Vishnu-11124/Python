

def twoSum(array, target):
    n = len(array)
    data_dict = {}

    for i in range(n):
        remaining = target - array[i]
        if remaining in data_dict:
            return [data_dict[remaining], i]
        data_dict[array[i]] = i

    return None

# -------------------------------------------------
        
print(twoSum([2, 7, 11, 15], 9))

# -------------------------------------------------

print(twoSum([5, 9, 1, 2, 4, 15, 6, 3], 13))

# -------------------------------------------------

print(twoSum([3, 1, 2, 4, 15, 6, 3], 6))

# -------------------------------------------------
