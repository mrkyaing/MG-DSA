products = []
n = int(input("How many products do you want to enter? "))
delimiter_format = " | "
for i in range(n):
    name = input(f"Enter product name {i+1}: ")
    products.append(name)
result = delimiter_format.join(products)
# if not result: #     print("No products entered.")
if not products:
    print("No products entered.")
else:
    print("Formatted product list: \n", result)