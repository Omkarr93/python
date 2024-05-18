class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage




class Bus(Vehicle):
    pass


schoolbus = Bus("volvo", 180, 20)
schoolbus1 = Bus("TATA",200,15)

print(schoolbus.name)
print(schoolbus1.max_speed)
