def calculate_discount(price, discount_rate):
    # Calculate the discount amount based on the price and discount rate.
    return price * discount_rate


def apply_discount(price, discount_amount):
    # Apply the discount amount to the original price and return the new price.
    return price - discount_amount


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        try:
            price = float(product["price"])
            discount_rate = float(product["discount_rate"])

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}\n")

        except ValueError:
            print(f"Error: Invalid price or discount rate for product '{product['name']}'.\n")
        except Exception as e:
            print(f"Unexpected error for product '{product['name']}': {e}\n")


if __name__ == "__main__":
    main()
