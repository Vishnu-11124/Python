# Print 'Mani kutty' 4 times

count = 0
def print_mani_kutty():
    global count
    if count == 4:
        return
    print('Mani kutty')
    count += 1
    print_mani_kutty()

print_mani_kutty()
