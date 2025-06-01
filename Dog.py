from Animal import Animal

class Dog(Animal):
    """inherits Animal class for its fields and methods

    Args:
        name (str): name of dog
        age (int): age of dog
    """
    def __init__(self, name, age):
        super().__init__(name, age)