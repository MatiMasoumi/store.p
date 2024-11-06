from store import Store
from phone import Phone
from laptop import Laptop
store = Store("Tech Store")
phone1 = Phone(name="iPhone 13", price=999.99, brand="Apple")
laptop1 = Laptop(name="Dell XPS", price=1299.99, brand="Dell",
                  memory="16GB", processor="Intel i7") 
store.add_data(phone1)
store.add_data(laptop1)
print("\nDisplaying all products:")
store.display()
phone1.apply_discount(10)
laptop1.apply_discount(15)
phone1.edit_product(name="iPhone 13 Pro")
laptop1.edit_product(price=1199.99)
print("\nDisplaying products after updates:")
store.display()
print("\nRemoving a product:")
store.remove(phone1.id)
store.display()
print("\nSearching for product by brand 'Dell':")
search_results = store.search(brand="Dell")
for result in search_results:
     print(result)
