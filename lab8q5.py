import numpy as np

# Create a 1D array with numbers from 1 to 16
arr = np.arange(1, 17)

# Reshape the array into a 4x4 matrix
matrix = arr.reshape(4, 4)

# Calculate the sum of each row
row_sums = matrix.sum(axis=1)

print("Original 1D array:", arr)
print("4x4 matrix:\n", matrix)
print("Sum of each row:", row_sums)
