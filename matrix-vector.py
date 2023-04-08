import numpy as np

matrix = np.array(
    [
        [1, 2, 3, 4],
        [1, 4, 5, 6],
        [1, 6, 7, 8],
        [1, 8, 9, 10],
    ]
)

vector = np.array(
    [0.5, 1, 2, 3]
)

result = np.dot(matrix, vector)

print(result)
