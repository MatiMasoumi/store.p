from product import Product

class Phone(Product):
    last_id=1000
    def __init__(self,name,price,brand):
        self.id=Phone.gen_id()
        super().__init__(self.id,name,price,brand)
    @classmethod
    def gen_id(cls):
         p_id="P" +str(cls.last_id)
         cls.last_id += 1
         return p_id
    def dis(self):
         print(f'{self.name}:is a phone.')
        