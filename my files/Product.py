from dataclasses import dataclass
@dataclass
class Product:
    product_name: str
    __price: float
    quantity: int
    discount: float
    @property
    def name(self):
        return self.product_name

    def __str__(self):
        if self.product_name != "":
            raise ValueError("Product name must be a string")
        else:
            return self.product_name


    def discount_price(self):
        return self

    def discount_quantity(self):
        if self.quantity > 0:
            raise ValueError("Quantity cannot be negative")
        else:
            self.discount =self.quantity
        return self

    @product_price.setter
    def total_price(self):
        if self.quantity > 0:
            raise ValueError("Quantity cannot be negative")
        else:
            self.__price = self.quantity
        return self


