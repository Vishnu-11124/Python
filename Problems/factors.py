
#  Normal solution
# def factors(number):
#     factors_list = []

#     for i in range(1, number + 1):
#         if number % i == 0:
#             factors_list.append(i)

#     return factors_list

# ------------------------------------------------------

# Optimized solution
def factors(number):
    factors_list = []
    half = number // 2

    for i in range(1, half + 1):
        if number % i == 0:
            factors_list.append(i)

    factors_list.append(number)

    return factors_list




# ------------------------------------------------------

print(factors(12))  # Output: [1, 2, 3, 4, 6, 12]

# -------------------------------------------------

print(factors(15))  # Output: [1, 3, 5, 15]

# -------------------------------------------------