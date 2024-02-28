import RetailItemClass as r

item1 = r.Retail('Jacket', 12, 59.95)
item2 = r.Retail('Designer Jeans', 40, 34.95)
item3 = r.Retail('Shirt', 20, 24.95)

print()
print(f"The first retail product is a {item1.get_descript()}, with {item1.get_units()} units on sale for ${item1.get_price()} each.")
print(f"The second retail product are {item2.get_descript()}, with {item2.get_units()} units on sale for ${item2.get_price()} each.")
print(f"The third retail product is a {item3.get_descript()}, with {item3.get_units()} units on sale for ${item3.get_price()} each.")
print()