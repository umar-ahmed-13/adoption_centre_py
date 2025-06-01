from User import User
from Animals import Animals
from Animal import Cat
from Animal import Dog
from Animal import Rabbit


class Customer(User):
    ADOPTION_LIMIT = 2
    """inherits user fields/ methods and has an adoption limit for animals for 2
    """

    def __init__(self, name, email):
        """creates a customer instance
        taking the name from user 
        also creates a list of adopted animals

        Args:
            name (str): name of customer
            email (str): email of customer
        """
        super().__init__(name)
        self.email = email
        self.adopted_animals = Animals()

    # returns adopted animals list
    def get_adopted_animals(self):
        return self.adopted_animals

    # returns customer email
    def get_email(self):
        return self.email

    def use(self, centre):
        """    
        Provides an interactive menu for the customer to access adoption center features.

        Displays options to view details, view animals, adopt an animal, or exit.
        Processes user input in a loop until the user chooses to log out.

        Args:
        centre (AdoptionCentre): The adoption center instance providing access to animals and other resources.
    
        """
        # Requires implementation
        print(self.customer_access_granted_message())
        print(self.customer_options_list())
        while True:
            print("Enter a choice (D/V/A/X): ", end="")
            customer_menu_choice: str = input().strip().upper()
            match customer_menu_choice:
                case "D":
                    self.details()
                    continue
                case "V":
                    self.view_animals(centre)
                    continue
                case "A":
                    animal_list = centre.animals.get_animals()
                    self.customer_adopt_animal(animal_list, centre)
                    continue
                case "X":
                    print(f"{self.get_name()} logged out successfully")
                    return
                case default:
                    print("Invalid input")
                    continue

   

    # views details of the customer and adopted animals
    def details(self):
        """
        Displays the customer's details and the list of animals they have adopted.

        Prints the customer's name and email, followed by a list of adopted animals.
        """
        # Requires implementation
        print("Customer Details\n----------------")
        print(f"{self.get_name()} ({self.get_email()})\n----------------")
        
        
        adopted_animal_list: list = self.get_adopted_animals().get_animals()
        if len(adopted_animal_list)!= 0:
            print("Adopted Animals")
            for animal in adopted_animal_list:
                print(animal)
  

    # views animals available for adoption
    def view_animals(self, centre):
        """
        Displays all animals available for adoption from the given adoption centre.

        Iterates through the animals in the centre and prints those that have not been adopted.

        Args:
            centre (AdoptionCentre): The adoption centre containing the animals.
        """
        animal_list: list = centre.animals.get_animals()
        print("Animals available for adoption:")
        for animal in animal_list:
            if not animal.is_already_adopted():
                print(animal)
     
    # customer menu options
    def customer_options_list(self) -> str:
        return """D :: View Your Details\nV :: View Adoptable Animals\nA :: Adopt an Animal\nX :: Logout"""

    # creates a new csutomer instance
    def create_new_customer(self, new_customer_name, new_customer_email) -> "Customer":
        return Customer(new_customer_name, new_customer_email)

    # message when customer successfully logs in
    def customer_access_granted_message(self) -> str:
        return f"Welcome to the customer menu {self.get_name()}, what would you like to do? "

    # adopts an animals from available animals
    def customer_adopt_animal(self, animal_list: list, centre):
        while True:
            print(self.customer_adopt_options(), end="")
            try:
                adopt_option: int = int(input().strip())
            except ValueError:
                print("Please input a valid integer")
                continue

            match adopt_option:
                case 1:
                    self.show_animals_available_for_adoption_and_adopt(animal_list, Cat, centre)
                    return
                case 2:
                    self.show_animals_available_for_adoption_and_adopt(animal_list, Dog, centre)
                    return
                case 3:
                    self.show_animals_available_for_adoption_and_adopt(animal_list, Rabbit, centre)
                    return
                case default:
                    print("Please enter a valid integer")

    # shows the animal types available for adoption
    def customer_adopt_options(self) -> str:
        return f"What type of animal are you looking to adopt?\n1. Cat\n2. Dog\n3. Rabbit\nEnter your choice: "

    # shows the particular animay type chosen and adopt
    def show_animals_available_for_adoption_and_adopt(self, animal_list: list, taken_type: "Animal", centre):
        print(f"{taken_type.__name__}s available for adoption:")  #important for printing type
        for animal in animal_list:
            if isinstance(animal, taken_type) and not animal.is_already_adopted():
                print(animal)
        print("Enter the name of the animal you would like to adopt: ", end="")

        animal_name: str = input().strip()

        self.check_animal_adopt(animal_name, taken_type, centre)  # centre reference
        return

    # checks if animal is available/ exists or if adoption limit reached
    def check_animal_adopt(self, taken_animal_name, taken_type, centre):
        adopted_animal_list = self.get_adopted_animals().get_animals()
        if len(adopted_animal_list) >= self.ADOPTION_LIMIT:
            print(
                f"Cannot adopt {taken_animal_name}, you have reached your adoption limit for {taken_type.__name__}s"
            )
            return

        retrieved_animal: Animal = self.find_animal(taken_animal_name, centre)

        if not retrieved_animal or retrieved_animal.is_already_adopted():
            print("No such animal is available for adoption")
            return
        print(f"{retrieved_animal.get_name()} has been adopted")
        retrieved_animal.adopt()
        self.adopted_animals.add(retrieved_animal)
        return

    # finds animal
    def find_animal(self, taken_name, centre):
        animal_list: list = centre.animals.get_animals()
        for animal in animal_list:
            if animal.get_name() == taken_name:
                return animal
        return None
