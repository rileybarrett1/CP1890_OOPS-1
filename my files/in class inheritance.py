from dataclasses import dataclass
from itertools import product


@dataclass
class Product:
    def product(self):
        name:str
        price: int
        discountpercent:int

    def discountamount(self,price:int):
        return price * (self.discountpercent / 100)
    def getdiscountprice(self):
        return self.price - self.discountamount

    def getdescription(self):
        return self.name

@dataclass
class book(product):
    author: str = ''


    def getdescription(self):
        return f"{product.getdescription()} by {self.author}"

    product1 = product("quarter marker",2.99,20)
    movie1 = product("the holy grail",6.99)
