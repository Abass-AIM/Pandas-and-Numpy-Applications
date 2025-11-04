import numpy as np

matrix = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 8, 9]
])

rows, cols = matrix.shape
main_diagonal = []

for i in range(rows):
    for j in range(cols):
        if i == j:   # main diagonal condition
            main_diagonal.append(int(matrix[i][j]))

print("Main Diagonal:", main_diagonal)



        