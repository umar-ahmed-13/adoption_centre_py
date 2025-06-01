from UnauthorizedAccessException import UnauthorizedAccessException
from Customer import Customer
from Users import Users
from Animals import Animals


class AdoptionCentre:
    def __init__(self, seed_animals, seed_users):
        self.animals = seed_animals
        self.users = seed_users

    def get_users(self):
        return self.users

    # use method for starting
    def use(self):
        # Start here
        """
        uses the adoption centre method
        """
        self.welcome_message()
        while True:
            print("Enter a choice (C/M/X): ", end="")
            choice: str = input().strip().upper()
            self.login(choice)
        # pass

    # startup message method
    def welcome_message(self) -> None:
        print(
            """Welcome to the Adoption Centre\nC :: Login as Customer\nM :: Login as Manager\nX :: Exit"""
        )

    # login options logic
    def login(self, choice):
        """handles login options logic

        Args:
            choice (string): choice taken in login 
        """
        match choice:
            case "C":
                self.handle_customer_login()  # handles login logic for customer
                return
            case "M":
                self.handle_manager_login()  # handles login logic for manager
                return
            case "X":
                print("Thank you for visiting the adoption centre")  # exit program
                exit()
            case default:
                print("Invalid Choice")
                return

    # manager login logic
    def handle_manager_login(self) -> None:
        """handles the manager login logic by taking manager ID and validating for login
        """
        print("Manager ID: ", end="")
        try:
            manager_id: int = int(input().strip())
        except ValueError:
            print("Please input integers only")
            return
        try:
            current_manager: Manager = self.users.validate_manager(manager_id)
            current_manager.use(self)
        except UnauthorizedAccessException:
            print("You are not authorized to access the manager menu")
            return

    # customer login logic
    def handle_customer_login(self) -> None:
        """handles the customer login logic by taking ID and pwd for login validation
        """
        while True:
            print("Please enter your customer credentials.")
            print("Name: ", end="")
            customer_name = input().strip()
            print("Email: ", end="")
            customer_email = input().strip()
            current_customer: Customer = self.users.validate_customer(
                customer_name, customer_email
            )
            if not current_customer:
                print(
                    "No such customer exists. Would you like to sign up with these credentials? (y/n) ",
                    end="",
                )
                create_new_customer_choice = input().strip().upper()
                if create_new_customer_choice == "Y":
                    new_customer: Customer = self.create_new_customer(
                        customer_name, customer_email
                    )
                    self.users.add(new_customer)
                    new_customer.use(self)
                    break

                elif create_new_customer_choice == "N":
                    continue
                else:
                    print("Invalid option, please use y/n")
            elif current_customer:
                current_customer.use(self)
                break


    # creates a new customer object
    def create_new_customer(
        self, new_customer_name: str, new_customer_email: str
    ) -> Customer:
        """used to create a new customer object

        Args:
            new_customer_name (str): takes name of customer
            new_customer_email (str): takes email od customer

        Returns:
            Customer: returns a new customer object created
        """
        return Customer(new_customer_name, new_customer_email)

    # used to run the code
if __name__ == "__main__":
    seed_animals = Animals().insert_seed_data()
    seed_users = Users().insert_seed_data(seed_animals)
    AdoptionCentre(seed_animals, seed_users).use()
