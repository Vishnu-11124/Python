
def setMatrixZero(array):
    rows = len(array)
    cols = len(array[0])

    row_track = [0] * rows
    col_track = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if(array[i][j] == 0):
                row_track[i] = -1
                col_track[j] = -1

    for k in range(rows):
        for l in range(cols):
            if(row_track[k] == -1 or col_track[l] == -1):
                array[k][l] = 0

    return array                         

# ---------------------------------------------------------------------------

# def setMatrixZero(array):
#     rows = len(array)
#     cols = len(array[0])

#     zeros_cols = set()
#     zeros_rows = set()

#     for i in range(rows):
#         for j in range(cols):
#             if(array[i][j] == 0):             
#                 zeros_rows.add(i)
#                 zeros_cols.add(j)

#     for k in zeros_rows:
#         for l in range(cols):
#             array[k][l] = 0    

#     for m in zeros_cols:
#         for n in range(rows):
#             array[n][m] = 0

#     return array                    

# ---------------------------------------------------------------------------

array =[[7, 9, 2, 3], [20, 8, 0, 10], [29, 0, -10, 5], [4, 14, 6, 7]]
print("Result", setMatrixZero(array))

# ---------------------------------------------------------------------------

array = [[7, 9, 2, 3], [20, 8, 0, 10], [29, 5, -10, 5], [4, 14, 6, 7]]
print("Result", setMatrixZero(array))

# ---------------------------------------------------------------------------

array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print("Result", setMatrixZero(array))

# ---------------------------------------------------------------------------
