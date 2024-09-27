# Maintainer: SP23_BAI_055
# Collaborator: SP23_BAI_031
class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        pass

    def make_purchase(self, quantity):
        if quantity < 0:
            raise ValueError("Cannot purchase negative quantity")
        if quantity > self.amount:
            raise ValueError(f"Only {self.amount} items in stock")
        
        total_price = self.get_price(quantity)
        self.amount -= quantity  # Reduce stock
        print(f"Total price: {total_price}")
        print(f"Remaining stock: {self.amount}")
