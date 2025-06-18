import numpy as np


n=int(input("Enter the number of elements you want to input: "))
# Take n numbers from the user
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

arr = np.array(numbers)

print("Array:", arr)
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
