
def merge_array(left_array, right_array):
    merged_array = []
    left_index, right_index = 0, 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merged_array.append(left_array[left_index])
            left_index += 1
        else:
            merged_array.append(right_array[right_index])
            right_index += 1

    merged_array.extend(left_array[left_index:])
    merged_array.extend(right_array[right_index:])
        

    # if left_index < len(left_array):
    #     while left_index < len(left_array):
    #         merged_array.append(left_array[left_index])
    #         left_index += 1

    # if right_index < len(right_array):
    #     while right_index < len(right_array):
    #         merged_array.append(right_array[right_index])
    #         right_index += 1

    return merged_array

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle_index = len(array) // 2
    left_array = merge_sort(array[:middle_index])
    right_array = merge_sort(array[middle_index:])

    return merge_array(left_array, right_array)

# -------------------------------------------------

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))

# Output: [3, 9, 10, 27, 38, 43, 82]

# -------------------------------------------------

print(merge_sort([5, 8, 2, 1, 4, 6]))

# Output: [1, 2, 4, 5, 6, 8]

# -------------------------------------------------
