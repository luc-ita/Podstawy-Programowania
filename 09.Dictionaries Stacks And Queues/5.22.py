import json


def get_input():
    product = dict()
    product['name'] = input("Enter the product name: ").strip()
    product['price'] = round(float(input("Enter the product price: ")), 2)
    paid_input = input("Has the product been paid for? (yes/no): ").lower().strip()
    product['paid'] = paid_input == 'yes'
    return product


def save_data(product):
    with open('product.json', 'w') as file:
        json.dump(product, file, indent=4)


product = get_input()
save_data(product)
