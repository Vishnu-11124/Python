
def binaryToDecimal(binary:str)->int:
    decimalNumber = 0
    power = 0
    index = len(binary) - 1
    while index >= 0:
        num = int(binary[index]) * (2 ** power)
        decimalNumber += num
        power += 1
        index -= 1
    return decimalNumber

# ----------------------------------------------------------------

decimal = binaryToDecimal("1101")
print("The result: ", decimal)  

# ----------------------------------------------------------------

decimal = binaryToDecimal("101101")
print("The result: ", decimal)  

