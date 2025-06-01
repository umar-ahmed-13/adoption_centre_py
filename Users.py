from Customer import Customer
from Manager import Manager
from UnauthorizedAccessException import UnauthorizedAccessException

class Users:
    # initializes a user with a users list
    def __init__(self):
        self.users = []
    
    # adds users to list
    def add(self, user):
        self.users.append(user)

    # returns users list
    def get_users(self):
        return self.users

    # these are the user seed data for testing
    def insert_seed_data(self, seed_animals):
        self.add(Customer("1", "1"))
        self.add(Manager("David Dyer", 12345))
        self.add(Manager("Rishik Sood", 48954))

        self.add(Customer("Dahyun Kim", "dahyun@twice.com"))
        self.add(Customer("Zyzz", "Aziz@gains.net"))

        daisy = Customer("Daisy Doodles", "daisy252gmail.com")
        nimo = [animal for animal in seed_animals.get_animals() if animal.get_name() == "Nimo"][0]
        daisy.get_adopted_animals().add(nimo)
        nimo.adopt()
        self.add(daisy)

        jenny = Customer("Jenny Jenson", "jenny123@gmail.com")
        oliver = [animal for animal in seed_animals.get_animals() if animal.get_name() == "Oliver"][0]
        jenny.get_adopted_animals().add(oliver)
        oliver.adopt()
        self.add(jenny)

        return self
    

    # these are the validate logins for customer
    def validate_customer(self, name, email):
        for user in self.users:
            if isinstance(user, Customer):
                if user.get_name() == name and user.get_email() == email:
                    return user
        return None
    
    # these are the validate logins for manager
    def validate_manager(self, manager_id):
        for user in self.users:
            if isinstance(user, Manager):
                if user.get_manager_id() == manager_id:
                    return user
        raise UnauthorizedAccessException()
