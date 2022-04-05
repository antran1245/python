import store
import product

# Store
store = store.Store("Happy")

# Product
carrot = product.Product("carrot", 3, "vegetable", 112)
apple = product.Product("apple", 2, "fruit", 223)
cake = product.Product("cake", 5, "baked sweet", 123)

# Put products into the store
store.add_product(carrot)
store.add_product(apple)
store.add_product(cake)

# Update price of cake
cake.update_price(.15, False)

# Print updated price of cake
cake.print_info()

# Sell the cake from store
store.sell_product(123)

# inflation
print("Inflation")
store.inflation(.2)
for product in store.products:
    print(f"{product.name} - {product.category} - ${product.price}")

# set clearance
print("Set Clearance")
store.set_clearance("fruit", .16)
for product in store.products:
    print(f"{product.name} - {product.category} - ${product.price}")