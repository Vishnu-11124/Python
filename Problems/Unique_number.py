A = [1, 3, 5, 7, 8]
B = [1, 2,  4, 6, 7, 8]

def unique_number(array_one, array_two):
    index = 0
    number = [0] * len(array_one)


    for i in array_one:
        unique = True   # reset here

        for j in array_two:
            if i == j:
                unique = False
                break

        if unique:
            number[index] = i
            index += 1
            

    return number[:index]

output = unique_number(A, B)
print("Unique numbers: ")
for j in output:
    print(j)
