'''
Instructions
Import numpy and assign to the alias np.
Assign the shape of vector to vector_shape.
Assign the shape of matrix to matrix_shape.
Display both vector_shape and matrix_shape using the print() function.
'''

import numpy as np
vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

vector_shape = vector.shape
matrix_shape = matrix.shape

print(vector_shape)
print(matrix_shape)

'''
    output:

    (3,)
    (3, 3)

'''
