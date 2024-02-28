import CellPhoneClass as c

phone = c.Cell('Apple', 'Iphone 15', 1099)

affirm = input(f"The Manufacturer is currently {phone.get_manufact()}. Do you want to change it? Enter 'yes' or 'no'.\n")
if affirm == 'yes':
    ma = input('Who is the Manufacturer? ') 
    phone.set_manufact(ma)
elif affirm == 'no':
    ma = phone._manufact
    phone.set_manufact(ma)

affirm = input(f"The Model is currently {phone.get_model()}. Do you want to change it? Enter 'yes' or 'no'.\n")
if affirm == 'yes':
    mo = input('What is the Model? ') 
    phone.set_model(mo)
elif affirm == 'no':
    mo = phone._model
    phone.set_model(mo)

affirm = input(f"The price is currently ${phone.get_retail_price()}. Do you want to change it? Enter 'yes' or 'no'.\n")
if affirm == 'yes':
    re = input('What is the price? ') 
    phone.set_retail_price(re)
elif affirm == 'no':
    re = phone._retail_price
    phone.set_retail_price(re)

print(f"{phone.get_manufact()} manufactured the {phone.get_model()} for a retail price of ${phone.get_retail_price()}.")
    
