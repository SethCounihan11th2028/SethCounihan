item = float(input("Enter the price of the item: "))
price = item
rate = float(0.06875)

tax = price * rate

print(f"{item} costs ${price} dollars before tax and ${price + tax} after tax")
