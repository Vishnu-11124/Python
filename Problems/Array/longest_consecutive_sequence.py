
def longestSequence(array):
    array_set = set()
    for i in array:
        array_set.add(i)
    max_length = 0

    for j in array_set:
        if j - 1 not in array_set:
            current_value = j
            current_length = 1
            while current_value + 1 in array_set:
                current_value += 1
                current_length += 1
                
            max_length = max(max_length, current_length)

    return max_length
   

# def longestSequence(array):
#     max_length = 0
#     for i in range(len(array)):
#         current_value = array[i]
#         current_length = 1
#         while current_value + 1 in array:
#             current_value += 1
#             current_length += 1
#         max_length = max(max_length, current_length)
#     return max_length

# def longestSequence(array):
#     array.sort()
#     count = 0
#     last_value = float("-inf")
#     max_length = 0

#     for i in array:
#         if i - 1 == last_value:
#             count += 1
#             last_value = i
#         else:
#             count = 1
#             last_value = i
#         max_length = max(max_length, count)

#     return max_length



# -------------------------------------------------

print(longestSequence([100, 4, 200, 1, 3, 2]))

# -------------------------------------------------

print(longestSequence([1, 99, 101, 98, 2, 5, 102, 97, 3, 100, 1, 2, 1]))

# -------------------------------------------------