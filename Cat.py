from Animal import Animal

class Cat(Animal):
    """inherits Animal class for its fields and methods

    Args:
        name (str): name of cat
        age (int): age of cat
    """
    def __init__(self, name, age):
        super().__init__(name, age)