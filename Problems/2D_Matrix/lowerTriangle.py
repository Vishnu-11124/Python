
def lower_Triangle(array):
    n = len(array)

    for i in range(n):
        for j in range(n):
            if j <= i:
                print(array[i][j], end=" ")
            else:
                print("*", end=" ")
        print()


# --------------------------------------------------

lower_Triangle([[5, 10, 8], [7, 6, 3], [2, 1, 9]])

# --------------------------------------------------

lower_Triangle([[5, 3, 9], [7, 1, 2], [5, 6, 1]])

# --------------------------------------------------
