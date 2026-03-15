
def maxConsecutiveOnes(array):
    total_count = new_count = 0

    for i in array:
        if i == 1:
            new_count += 1
        
        else:
            if new_count > total_count:
                total_count = new_count
            new_count = 0  

    if new_count > total_count:
        total_count = new_count        

    return total_count           

# -------------------------------------------------

print(maxConsecutiveOnes([1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1]))

# -------------------------------------------------

print(maxConsecutiveOnes([1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]))

# -------------------------------------------------


        
