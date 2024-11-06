from abc import ABC,abstractmethod
class Product(ABC):
    def __init__(self,id_,name,price,brand):
        self.id=id_
        self.name=name
        self.price=price
        self.brand=brand
    def __str__(self):
        return f"name:{self.name},price:{self.price},brand:{self.brand}"
    @abstractmethod 
    def dis(self):
        """
        abstract method to display tp product information
        """
        pass
    def edit_product(self,name=None,price=None,brand=None):
        """
        edit the phone's attributes if new valus are provide
        """
        self.name=name or self.name
        self.price=price or self.price
        self.brand=brand or self.brand
    def apply_discount(self,discount):
        if 0 <= discount <= 100:
            discount_amount=self.price * (discount/100)
            self.price -= discount_amount
            print(f'discount:{discount}% applied. new price:{self.price}')
        else:
            print('Invalid discount')
