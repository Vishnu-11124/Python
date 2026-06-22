
def transpose(matrix):
    cols = len(matrix[0])
    rows = len(matrix)

    transpose = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose

# --------------------------------------------------

print(transpose([[3, 6, 7], [7, 9, 2]]))

# --------------------------------------------------

print(transpose([[8, 12, 10], [23, 2, 7], [43, 18, 87], [4, 42, 67]]))

# -------------------------------------------------- 