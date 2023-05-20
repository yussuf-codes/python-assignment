from classes.Product import Product
from classes.Stock import Stock

product1 = Product(1, 'Chicken', 'Kilo', 40, 80)
product2 = Product(2, 'Coffee', 'Kilo', 15, 300)
product3 = Product(3, 'Eggs', 'Package', 60, 50)
product4 = Product(4, 'Pepsi', 'Liter', 120, 15)

myStock = Stock()

myStock.insert(product1)
myStock.insert(product2)
myStock.insert(product3)
myStock.insert(product4)

# all products
# myStock.AllProducts()

# product by id
# x = myStock.getProduct(2)
# print(x)
# x.setQuantity(5)
# print(x)