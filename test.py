import product as PRODUCT, store as STORE

store = STORE.Store("Store_1")
print(store.name)

product1 = PRODUCT.Product("Product_1", 5, "Fruit", "FRUITY")
product2 = PRODUCT.Product("Product_2", 10, "Vegetable", "VEGGIE")
product3 = PRODUCT.Product("Product_3", 15, "MEAT", "MEATY")

product1.update_price(0.1, True).print_info()
product2.update_price(0.1, True).print_info()
product3.update_price(0.1, True).print_info()

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

store.inflation(0.1)

for x in range(len(store.list_products)):
    store.list_products[x].print_info()

store.set_clearance("Fruit", 0.1)
product1.print_info()

store.sell_product("FRUITY")