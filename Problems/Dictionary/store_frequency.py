
def store_frequency(word_list):
    frequency_dict = {}
    for word in word_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

# ------------------------------------------------------

word_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
result = store_frequency(word_list)
print(result)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# ------------------------------------------------------

word_list = [2, 3, 2, 5, 3, 2, 8, 9, 5]
result = store_frequency(word_list)
print(result)  # Output: {2: 3, 3: 2, 5: 2, 8: 1, 9: 1}     

# ------------------------------------------------------
