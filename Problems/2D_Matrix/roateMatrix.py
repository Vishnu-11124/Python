
def rotate(matrix):
    n = len(matrix)

    for i in range(n-1):
        for j in range(i + 1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()   

    return matrix        
# ---------------------------------------------------------------------------

# def rotate(matrix):
#     n = len(matrix)
#     new_matrix = [[0] * n for _ in range(n)]

#     for i in range(n):
#         k = n - 1 - i
#         for j in range(n):
#             new_matrix[j][k] = matrix[i][j]

#     return new_matrix

# --------------------------------------------------------

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))

# --------------------------------------------------------

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))

# --------------------------------------------------------
