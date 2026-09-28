
item = input("What item are you buying?\n ")
item_price =float(input("How much does it cost?\n "))
rate = 1.06875

def calculate_tax(item, price, rate):
    print(item + "costs $" + str(price) + " before tax and $" + str(round(item_price * rate, 2)) + " after tax.")

calculate_tax(item, item_price, rate)