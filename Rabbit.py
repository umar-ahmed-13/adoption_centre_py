from Animal import Animal

class Rabbit(Animal):
    """inherits Animal class for its fields and methods

    Args:
        name (str): name of rabbit
        age (int): age of rabbit
    """
    def __init__(self, name, age):
        super().__init__(name, age)