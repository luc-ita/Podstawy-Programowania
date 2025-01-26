# Initial price list
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}



print("Products and Prices Before Discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")



total_before_discount = sum(price_list.values())
print(f"\nTotal value of products before discount: ${total_before_discount:.2f}")



for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)


print("\nProducts and Prices After 10% Discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")


total_after_discount = sum(price_list.values())
print(f"\nTotal value of products after discount: ${total_after_discount:.2f}")
