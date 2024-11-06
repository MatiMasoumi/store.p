from product import Product

class Laptop(Product):
    last_id=1000
    def __init__(self,name,price,brand,memory,processor):
        self.id=Laptop.gen_id()
        super().__init__(self.id,name,price,brand)
        self.memory=memory
        self.processor=processor
    @classmethod
    def gen_id(cls):
         L_id="L" +str(cls.last_id)
         cls.last_id += 1
         return L_id
    def __str__(self):
         return f'{super().__str__()},memory:{self.memory},processor:{self.processor}'
    def dis(self):
         print(f'{self.name}:is a laptop.')
        