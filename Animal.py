class Animal:
    # constructs the animal object with name and age and adoption status false
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.adopted = False


    # returns name
    def get_name(self):
        return self.name
    
    # returns bool of the adoption state
    def is_already_adopted(self):
        return self.adopted
    
    # marks animal as adopted
    def adopt(self):
        self.adopted = True

    # overrides the to string method to show name and age
    def __str__(self):
        return f"{self.name} (Age: {self.age})" #important change in string method

# these classes inherit the animal class and has constructed corresponding objects
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

class Rabbit(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)