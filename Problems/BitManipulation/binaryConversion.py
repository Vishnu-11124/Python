
def binaryConversion(num:int)-> str:
    result = ""
    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        num = num // 2

    result = result[::-1]
    return result

# -----------------------------------------------------------

binary = binaryConversion(13)
print("The binary value of 13: ", binary) 

# -----------------------------------------------------------

binary = binaryConversion(24)
print("The binary value of 24: ", binary) 