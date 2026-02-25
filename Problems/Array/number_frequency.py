

def number_frequency(first_list, second_list):
    freq_list = {}
    
    # Create a frequency count of the second list
    second_list_freq = {}
    for num in second_list:
        second_list_freq[num] = second_list_freq.get(num, 0) + 1
    
    # Check each number in the first list against the frequency map
    for i in first_list:
        freq_list[i] = second_list_freq.get(i, 0)
    
    return freq_list


# -------------------------------------------------

one = [1, 2, 3, 4, 5]
two = [1, 1, 2, 3, 4, 5, 5, 5]

print(number_frequency(one, two))

# ------------------------------------------------- 

three = [1, 2, 3, 4, 5]
four = [1, 1, 2, 3, 4, 2, 3, 4, 5, 5, 5]

print(number_frequency(three, four))

# -------------------------------------------------