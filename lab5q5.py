# 1. Use a while loop to create a list of even numbers from 2 to 20
numbers = []
n = 2
while n <= 20:
    numbers.append(n)
    n += 2

# 2. Use a for loop to calculate the sum of the squares of those numbers
sum_squares = 0
for num in numbers:
    sum_squares += num ** 2

# 3. Print the result
print(f"Sum of the squares of even numbers from 2 to 20 is {sum_squares}")