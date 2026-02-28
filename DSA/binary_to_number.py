def binary_to_number(number):
    value = 0
    power = 0

    # Convert binary string to decimal
    for i in number[::-1]:
        if i == '1':          # compare with string
            value = value + (2 ** power)
        power += 1

    # Count steps
    step = 0
    while value > 1:
        if value % 2 == 0:
            value = value // 2   # integer division
        else:
            value = value + 1
        step += 1

    return step


# ------------------------------------------------------

print("Steps:", binary_to_number("1101"))  # Output: Steps: 3  

# ------------------------------------------------------

print("Steps:", binary_to_number("10"))  # Output: Steps: 1

# ------------------------------------------------------
