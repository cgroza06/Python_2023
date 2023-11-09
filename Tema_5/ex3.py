class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model= model
        self.year= year

class Car(Vehicle):
    def __init__(self, make, model, year, mileage, towing_capacity):
        super().__init__(make, model, year)
        self.mileage =  mileage
        self.towing_capacity= towing_capacity

    def calculate_mileage(self):
        return self.mileage

    def calculate_towing_capacity(self):
        return self.towing_capacity

    def __str__(self):
        return f" Car made by {self.make}, model = {self.model}, year = {self.year}, mileage = {self.mileage} miles per liter, towing_capacity = {self.towing_capacity} kg"


class MotorCycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return self.mileage

    def __str__(self):
        return f" Motorcycle made by {self.make}, model = {self.model}, year = {self.year}, mileage = {self.mileage} miles per liter"

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return self.towing_capacity

    def __str__(self):
        return f" Truck made by {self.make}, model = {self.model}, year = {self.year},  towing_capacity = {self.towing_capacity} kg"

car= Car("Dacia", "Logan", 2002, 30, 500)
print(car)
motor = MotorCycle("Suzuky", "2", 2009, 100)
print(motor)
truck = Truck("MAN", "modelNou", 2020, 2000)
print(truck)
