import array as arr

numbers = arr.array('i', [1, 2, 3, 4, 5])

print("Available numbers: ")
for i in numbers:
    print(i, end =" ")
print()

print("Array length: ",len(numbers))    

# ------------------------------------------------------
new_numbers = numbers[::-1]
print("Reverse array: ",new_numbers)