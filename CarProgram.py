import CarClass as c

car = c.Car(2019, 'Jeep Cherokee')

print()
print(f"Let's speed this {car.year_model} {car.make} up!")
print()

car.accelerate()
print(f" The car speed is {car.get_speed()}")

car.accelerate()
print(f" The car speed is {car.get_speed()} mph")

car.accelerate()
print(f" The car speed is {car.get_speed()} mph")

car.accelerate()
print(f" The car speed is {car.get_speed()} mph")

car.accelerate()
print(f" The car speed is {car.get_speed()} mph")

print()
print(f"Slow your horses! Let's slow this {car.year_model} {car.make} down.")
print()

car.brake()
print(f"The car speed is {car.get_speed()} mph")

car.brake()
print(f"The car speed is {car.get_speed()} mph")

car.brake()
print(f"The car speed is {car.get_speed()} mph")

car.brake()
print(f"The car speed is {car.get_speed()} mph")

car.brake()
print(f"The car speed is {car.get_speed()} mph")


