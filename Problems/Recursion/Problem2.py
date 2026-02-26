
def print_numbers(start, end):
    if start > end:
        return
    print(start)
    print_numbers(start + 1, end)

print_numbers(1, 5)
    