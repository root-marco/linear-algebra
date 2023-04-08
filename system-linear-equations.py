import numpy as np

A = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)

b = np.array([1, 2, 3])

if np.linalg.matrix_rank(A) == A.shape[0]:
    x = np.linalg.solve(A, b)
    print(x)
else:
    print("The matrix A does not have full rank, cannot find a unique solution.")
