
def string_palindrome(string):
    
    left = 0
    right = len(string) - 1

    flag = True

    while left < right:
        if string[left] != string[right]:
            return "The string is not a palindrome."
        left += 1
        right -= 1

    return "The string is a palindrome."

        

# ------------------------------------------------------

print(string_palindrome("madam"))  # Output: The string is a palindrome.

# ------------------------------------------------------

print(string_palindrome("hello"))  # Output: The string is not a palindrome.

# ------------------------------------------------------