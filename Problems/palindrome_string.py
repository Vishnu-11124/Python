
def string_palindrome(string):
    
    left = 0
    right = len(string) - 1

    flag = True

    while left < right:
        if string[left] != string[right]:
            flag = False
            break
        left += 1
        right -= 1

    if flag:
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."

# ------------------------------------------------------

print(string_palindrome("madam"))  # Output: The string is a palindrome.

# ------------------------------------------------------

print(string_palindrome("hello"))  # Output: The string is not a palindrome.

# ------------------------------------------------------