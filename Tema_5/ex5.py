class Animal:
    def __int__(self,name, species):
        self.name = name
        self.species = species

    def nr_of_legs(self):
        pass

    def make_sound(self):
        pass

    def __str__(self):
        return f"Name={self.name}, Species={self.species}"

class Fish(Animal):
    def __init__(self, name, species, water_type):
        super().__int__(name, species)
        self.water_type = water_type

    def nr_of_legs(self):
        return 0

    def make_sound(self):
        return "Blub"

    def __str__(self):
        return f"{super().__str__()}, Water Type={self.water_type}"

class Mammal(Animal):
    def __init__(self, name, species, speed):
        super().__int__(name, species)
        self.speed = speed

    def make_sound(self):
        return "A lot of sounds"

    def __str__(self):
        return f"{super().__str__()}, Speed ={self.speed}"

class Bird(Animal):
    def __init__(self, name, species, fly):
        super().__int__(name, species)
        self.fly = fly

    def make_sound(self):
        return "Chirp"

    def __str__(self):
        return f"{super().__str__()}, Fly ={self.fly}"


fish1 = Fish("Nemo", "Clownfish", "Saltwater")
mammal1 = Mammal("Simba", "Lion", "Fast")
bird1 = Bird("Rio", "Spix's macaw", "Yes")