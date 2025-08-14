def calculate_discount(price, discount_percent):
    discount_rate = discount_percent / 100
    return price - (price*discount_rate)

price = int(input("Enter the original price: "))
discount_percent = int(input("The the percentage discount: "))

if discount_percent >= 20:
    discounted_price = (calculate_discount(price, discount_percent))
    print (f"The discounted price is: {discounted_price}")

else:
    print("Sorry,the eligible discount percentage should be 20% and above")
    print(f"Price remains {price}")

print("Thank you")
