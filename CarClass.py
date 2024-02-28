class Car:

    def __init__(self,yr,mk):
        self.year_model = yr
        self.make = mk
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed
    
        
