
def count_number(number):
    if number == 0:
        return 1
    count = 0
    new_number = number
    while new_number > 0:
        count += 1
        new_number = new_number // 10
    return count



# ------------------------------------------------------

print(count_number(12345))  # Output: 5

# ------------------------------------------------------

print(count_number(0))  # Output: 1

# ------------------------------------------------------

print(count_number(9876543210))  # Output: 10