from User import User
from Animal import Cat
from Animal import Dog
from Animal import Rabbit


class Manager(User):

    def __init__(self, name, manager_id):
        """
        Initialize a Manager instance.

        Args:
            name (str): The name of the manager.
            manager_id (int or str): A unique identifier for the manager.

        This constructor calls the superclass initializer with the manager's name
        and sets the manager's ID.
        """
        super().__init__(name)
        self.manager_id = manager_id

    def get_manager_id(self):
        """
        Retrieve the manager's unique identifier.

        Returns:
            int or str: The manager's ID.
        """
        return self.manager_id

    def use(self, centre):
        """
        Provides an interactive menu for the manager to perform actions on the adoption centre.

        Args:
            centre (AdoptionCentre): The adoption centre instance on which the manager will operate.

        This method prints access granted messages and options, then enters a loop
        prompting the manager to enter commands until the exit command is given.
        """
        print(self.manager_access_granted_message())
        print(self.manager_options_list())

        # the options loop
        while True:
            print("Enter choice (D/V/A/R/X): ", end="")
            manager_choice: str = input().strip().upper()
            continue_loop = self.manager_options(manager_choice, centre)
            if not continue_loop:
                break
        return

  

    def details(self):
        """
        Display the manager's details.

        Prints the manager's name followed by the role designation "(Manager)".
        """
        print(f"{self.get_name()} (Manager)")
     

    def view_animals(self, centre):
        """
        Display all animals currently in the adoption centre.

        Args:
            centre (AdoptionCentre): The adoption centre whose animals are to be listed.

        Prints each animal's details retrieved from the centre's animal collection.
        """
        print("All animals in the adoption centre")
        for animal in centre.animals.get_animals():
            print(animal)
     

    def manager_access_granted_message(self) -> str:
        """
        Generate a welcome message for the manager upon accessing the manager menu.

        Returns:
            str: A personalized welcome message including the manager's name.
        """
        return (
            f"Welcome to the manager menu {self.get_name()}, what would you like to do?"
        )

    # manager options after login
    def manager_options_list(self) -> str:
        return "D :: View Your Details\nV :: View Animals\nA :: Add an Animal\nR :: Remove an animal\nX :: Logout"

    # the manager options switch
    def manager_options(self, option, taken_centre) -> bool:
        match option:
            case "D":
                self.details()
                return True
            case "V":
                self.view_animals(taken_centre)
                return True
            case "A":
                self.manager_add_animal(taken_centre)
                return True
            case "R":
                print(self.remove_animal(taken_centre))
                return True
            case "X":
                print(f"{self.get_name()} successfully logged out")
                return False
            case default:
                print("Invalid choice")
                return True

    # add animal
    def manager_add_animal(self, taken_centre):
        while True:
            print("Animal Name: ", end="")
            animal_name: str = input().strip()
            print("Animal Age: ", end="")
            try:
                animal_age: int = int(input())
            except ValueError:
                print("Please enter a valid animal age")
                continue
            print("Animal Type: ", end="")
            animal_object: Animal = self.read_animal_type(animal_name, animal_age)
            if animal_object is not None:
                taken_centre.animals.add(animal_object)
                print(
                    f"{animal_object.get_name()} successfully added to the adoption centre"
                )
                break
            else:
                continue

    # read animal type
    def read_animal_type(self, name, age):
        type_input: str = input().strip().upper()
        match type_input:
            case "CAT":
                return Cat(name, age)
            case "DOG":
                return Dog(name, age)
            case "RABBIT":
                return Rabbit(name, age)
            case default:
                print("Please input a valid animal type")
                return None
   
    # remove animal method
    def remove_animal(self, centre) -> str:
        print("Enter name of animal to remove: ", end="")
        animal_name: str = input().strip()
        found: bool = False
        for animal in centre.animals.get_animals():

            taken_animal: Animal = animal
            if (
                taken_animal.is_already_adopted() == True
                and taken_animal.get_name() == animal_name
            ):
                return f"Cannot remove {taken_animal.get_name()}, they have already been adopted"

            elif (
                taken_animal.is_already_adopted() == False
                and taken_animal.get_name() == animal_name
            ):
                found = True
                centre.animals.remove(taken_animal)
                return f"{taken_animal.get_name()} successfully removed from the adoption centre"

        if not found:
            return f"{animal_name} not found"
