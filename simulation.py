import products
import store

walmart = store.Store('Walmart')
iphone = products.Products('Apple iPhone', 100, 'Electronics', 1123)
galaxy = products.Products('Samsung Galaxy', 125, 'Electronics', 100)
newPhone = products.Products('Omega 10 Phone', 500, 'Electronics', 51)

walmart.add_products(iphone).add_products(galaxy).add_products(newPhone)
walmart.inflation(0.10)
walmart.set_clearance('Electronics',0.25)

target = store.Store('Target')
milk = products.Products('1 Gallon', 20, 'Dairy', 11)
icecream = products.Products('1 Tub of Icecream', 5, 'Dairy', 25)

target.add_products(milk).add_products(icecream).add_products(iphone).add_products(galaxy).add_products(newPhone)
target.sell_products(25)
walmart.sell_products(1123)