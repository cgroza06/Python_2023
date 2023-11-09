import random
class Animal:
    def __init__(self, age, weight, race):
        self.age = age
        self.weight = weight
        self.race = race

    def __str__(self):
        return f"{self.race} is {self.age} old and weighs {self.weight} "


class Mammal(Animal):
    def __init__(self, age, weight, race, fur_color):
        super().__init__(age, weight, race)
        self.fur_color = fur_color

    def give_birth(self):
        random_number = random.randint(1, 7)
        return f"{self.race} gives birth to {random_number}"

    def __str__(self):
        animal_str=super().__str__()
        return f"{animal_str}, fur color: {self.fur_color}"

class Bird(Animal):
    def __init__(self, age, weight, race, eggs_size):
        super().__init__(age, weight, race)
        self.eggs_size = eggs_size
        self.distance = 0

    def fly(self, distance):
        self.distance+=distance
        return f"{self.race} flew {self.distance} in total"

    def __str__(self):
        animal_str = super().__str__()
        return f"{animal_str}, eggs size: {self.eggs_size}"


class Fish(Animal):
    def __init__(self, age, weight, race, predatory):
        super().__init__(age, weight, race)
        self.predatory = predatory

    def is_predatory(self):
        if self.predatory:
            return "is predatory"
        else:
            return "is not predatory"

    def __str__(self):
        animal_str = super().__str__()
        return f"{animal_str}, is predatory: {self.is_predatory()}"


vaca = Mammal(2, 120, "vaca", "alb cu negru")
gaina = Bird(1, 1, "gaina", "medium")
pastrav = Fish(2, 0.7, "pastrav", True)

print(vaca)
print(gaina)
print(pastrav)

print(vaca.give_birth())
print(gaina.fly(5))
print(pastrav.is_predatory())
print(gaina.fly(10))
