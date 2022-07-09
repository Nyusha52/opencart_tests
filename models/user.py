import random

from faker import Faker

fake = Faker("Ru-ru")


class RegistrData:

    def __init__(self, name=None, lastname=None, email=None, password=None, telephone=None):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.telephone = telephone

    @staticmethod
    def random():
        name = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        password = f"ANrb{random.randint(0, 1000)}"
        telephone = fake.random.randint(5550, 100000000)
        return RegistrData(name, lastname, email, password, telephone)
