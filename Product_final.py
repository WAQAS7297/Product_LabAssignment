# Maintainer: SP23_BAI_055
# Collaborator: SP23_BAI_031
class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        elif quantity < 10:
            return self.price * quantity
        elif 10 <= quantity < 100:
            return self.price * quantity * 0.9 
        else:
            return self.price * quantity * 0.8  

    def make_purchase(self, quantity):
        if quantity < 0:
            raise ValueError("Cannot purchase negative quantity")
        if quantity > self.amount:
            raise ValueError(f"Only {self.amount} items in stock")
        
        total_price = self.get_price(quantity)
        self.amount -= quantity 
        print(f"Total price: {total_price}")
        print(f"Remaining stock: {self.amount}")
