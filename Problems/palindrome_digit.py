
def palindrome_digit(number):
    if number == 0:
        return "The number is a palindrome. It's zero."
    
    original_number = number
    reversed_number = 0

    while number > 0:
        reversed_number = (reversed_number * 10) + (number % 10)
        number = number // 10

    if original_number == reversed_number:
        return "The number is a palindrome."
    else:
        return "The number is not a palindrome."


# ------------------------------------------------------

print(palindrome_digit(12321))  # Output: The number is a palindrome.

# ------------------------------------------------------

print(palindrome_digit(12345))  # Output: The number is not a palindrome.

# ------------------------------------------------------

print(palindrome_digit(0))  # Output: The number is a palindrome. It's zero.

# ------------------------------------------------------

print(palindrome_digit(7))  # Output: The number is a palindrome.