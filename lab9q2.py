# Create a string of numbers from 1 to 10,000, joined by commas
delimiter = ','
numbers_str = delimiter.join([str(i) for i in range(1, 10001)])
print(numbers_str)
