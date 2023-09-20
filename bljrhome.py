class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        self.items = [(p, q) for p, q in self.items if p != product]

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

def main():
    # Create some example products
    product1 = Product("Apple", 0.5, 10)
    product2 = Product("Banana", 0.3, 20)
    product3 = Product("Orange", 0.4, 15)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(product1, 2)
    cart.add_item(product2, 3)
    cart.add_item(product3, 1)

    # Remove an item from the cart
    cart.remove_item(product2)

    # Calculate and print the total
    total = cart.calculate_total()
    print("Total: $", total)

if __name__ == "__main__":
    main()
