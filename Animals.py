from Animal import Cat
from Animal import Dog
from Animal import Rabbit

class Animals:
    """creating animals instance with a lsit of animals and 
    using seed data for testing
    """
    def __init__(self):
        self.animals = []

    # add animal to list
    def add(self, animal):
        self.animals.append(animal)

    # remove animal from list
    def remove(self, animal):
        self.animals.remove(animal)

    # returns animal list
    def get_animals(self):
        return self.animals
        
    # these are the seed data for the animals for testing
    def insert_seed_data(self):
        self.add(Cat("Jiu Jiu", 5))
        self.add(Cat("Abby", 8))
        self.add(Cat("Nimo", 6))
        self.add(Cat("Whiskers", 3))
        self.add(Cat("Luna", 7))
        self.add(Cat("Oliver", 2))
        self.add(Cat("Mochi", 1))
        self.add(Cat("Simba", 6))

        self.add(Dog("Charlie", 2))
        self.add(Dog("Buddy", 4))
        self.add(Dog("Bella", 1))
        self.add(Dog("Max", 7))
        self.add(Dog("Rocky", 8))
        self.add(Dog("Milo", 5))

        self.add(Rabbit("Carrots", 1))
        self.add(Rabbit("Coco", 6))
        self.add(Rabbit("BunBun", 2))
        self.add(Rabbit("Hazel", 2))
        self.add(Rabbit("Peanut", 3))

        return self

