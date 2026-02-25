

def armstrong_number(number):
    original_number = number  # Store the original number for later comparison

    # Step 1: Find the number of digits
    temp = number  # Use temp to count digits
    count = 0

    while temp > 0:
        temp //= 10
        count += 1

    # Step 2: Calculate the sum of each digit raised to the power 'count' using the original number
    total_sum = 0

    while number > 0:
        digit = number % 10
        total_sum += digit ** count
        number //= 10  # Update number each iteration

    # Step 3: Compare the sum with the original number
    if total_sum == original_number:
        return "The number is an Armstrong number."
    else:
        return "The number is not an Armstrong number."


# ------------------------------------------------------

print(armstrong_number(153))

# ------------------------------------------------------

print(armstrong_number(123))

# -------------------------------------------------
