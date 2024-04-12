from dataclasses import dataclass


@dataclass
class ProductViewer:
    def __init__(self):
        self.products = ["stanley 13 ounce wood hammer", "economy duct tape,60 yds, silver",
                         "national hardware 3/4 wire nails"]

        self.price: float
        self.discount_percent: int
        self.discount_amount: float

    def display_products(self):
        for n, products in enumerate(self.products):
            print(products)

    def display_price(self, price, discount_percent):
        self.discount_amount = price * discount_percent
        print(self.discount_amount)


class Prices:
    def price(self, hammer, duct_tape, national_hardware):
        self.setattr() = 12.99
        self.duct_tape = 8.99
        self.national_hardware = 5.99

    def discount(self):
        self.hammer_discounted = 62
        self.duct_discounted = 50
        self.national_hardware_discounted = 40
        self.discount_price = self.discount_amount - self.price
        return self.discount_price
