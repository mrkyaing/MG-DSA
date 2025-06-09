price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))
vat_rate = 0.07
subtotal = price * quantity
vat = subtotal * vat_rate
total = subtotal + vat
print(f"Total payment (including 7% VAT): {total:.2f}")