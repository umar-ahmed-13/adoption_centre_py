from abc import abstractmethod

# abstract class that outlines what users should be able to do

class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    @abstractmethod
    def details():
        pass

    @abstractmethod
    def use(centre):
        pass

    @abstractmethod
    def view_animals(centre):
        pass
    
 
