class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f"Year={self.year}, Make={ self.make}, Model={self.model}",end=' ')

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def print_info(self):
        super().print_info()
        print(f"Doors={self.doors}" )


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, seats):
        super().__init__(make, model, year)
        self.seats = seats

    def print_info(self):
        super().print_info()
        print(f"Seats={self.seats}")

class Truck(Vehicle):
    def __init__(self, make, model, year,engine):
        super().__init__(make, model, year)
        self.engine = engine

    def print_info(self):
        super().print_info()
        print(f"Engine={self.engine}")

car1 = Car("Toyota", "Camry", 2018, 4)
car1.print_info()

motorcycle1 = Motorcycle("Honda", "Goldwing", 2018, 2)
motorcycle1.print_info()

truck1 = Truck("Ford", "F150", 2018, "V8")
truck1.print_info()