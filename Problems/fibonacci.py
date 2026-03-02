
def fibonacci_number( number):
    if number < 0:
        return "Input should be a non-negative integer."
    elif number == 0 or number == 1:
        return number
    else:
        return fibonacci_number(number - 1) + fibonacci_number(number - 2)
    
# ------------------------------------------------------

print(fibonacci_number(10))  # Output: 34

# ------------------------------------------------------

print(fibonacci_number(0))   # Output: 0

# ------------------------------------------------------

print(fibonacci_number(1))   # Output: 1

# ------------------------------------------------------

print(fibonacci_number(2))   # Output: 1

# ------------------------------------------------------
