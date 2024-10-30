class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    def display_info(self):
        print(f"{self.__class__.__name__} - Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")
    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=80, happiness=60)
        self.aggressiveness = 70

    def feed(self):
        self.health += 15
        self.happiness += 5

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=70)
        self.speed = 90

    def feed(self):
        self.health += 5
        self.happiness += 15

class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=60, happiness=100)
        self.horn_length = 40

    def feed(self):
        self.health += 5
        self.happiness += 30

zoo1 = Zoo("Omar's Zoo")

zoo1.add_animal(Lion("Ameed", 5))
zoo1.add_animal(Lion("Loai", 4))
zoo1.add_animal(Tiger("Jalal", 3))
zoo1.add_animal(Tiger("Ali", 6))
zoo1.add_animal(Elephant("Sami", 2))

zoo1.print_all_info()

for animal in zoo1.animals:
    animal.feed()

zoo1.print_all_info()