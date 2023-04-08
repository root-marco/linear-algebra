import numpy as np

matrix = np.array(
    [
        [1, 2],
        [3, 4],
    ]
)

determinant = np.linalg.det(matrix)
print (f'determinant = {determinant}')

if determinant != 0:
    inverse = np.linalg.inv(matrix)
    print (f'inverse = \n{inverse}')
else:
    print("Matrix is singular, cannot find inverse.")
