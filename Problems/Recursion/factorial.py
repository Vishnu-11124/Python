

def number_factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * number_factorial(number - 1)

# ------------------------------------------------------    

print("Factorial of 5 is :",number_factorial(5))

# ------------------------------------------------------

print("Factorial of 10 is :",number_factorial(10))

# -------------------------------------------------

print("Factorial of 0 is :",number_factorial(0))
print("Factorial of 1 is :",number_factorial(1))

# ------------------------------------------------------