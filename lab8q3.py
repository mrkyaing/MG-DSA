import numpy as np
# define a 3x3 matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
identity_matrix = np.eye(3)
# product of  matix
product_matrix = np.dot(matrix, identity_matrix)
print("Product of the matrix with itself:\n", product_matrix)
# find the identity matrix
print("Identity matrix:\n", identity_matrix)
