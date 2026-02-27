# Parameterized Recursion

def sum_numbers(sum, start, end):
    if start > end:
        print("sum :",sum)
        return 
    sum_numbers(sum + start, start + 1, end)


sum_numbers(0, 1, 5)