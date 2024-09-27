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
            return self.price * quantity * 0.9  # 10% discount
        else:
            return self.price * quantity * 0.8  # 20% discount

    def make_purchase(self, quantity):
        pass
