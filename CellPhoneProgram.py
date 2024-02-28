import CellPhoneClass as c

cell = c.Cell()

man = input('Who is the Manufacturer? ')
cell.set_manufact(man)

model = input('What is the model? ')
cell.set_model(model)

retail = input('What is the retail price? ')
cell.set_retail_price(retail)

print(f"{cell.get_manufact()} manufactured the {cell.get_model()} for a retail price of ${cell.get_retail_price()}")
    
