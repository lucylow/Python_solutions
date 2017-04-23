# Classes and cars 


class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)
        
    def drive_car(self):
        self.condition = "used"
        
        
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
        
    def drive_car(self):
        self.condition = "like new"
        
    
# testing 
my_car = Car("DeLorean", "silver", 88)

print my_car.condition
my_car.drive_car()
print my_car.condition

my_car = ElectricCar("my_car", "Green", 170, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition
