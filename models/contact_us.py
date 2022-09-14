import random

from faker import Faker

fake = Faker("Ru-ru")


class ContactUsData:

    def __init__(self, name=None, email=None, enquiry=None):
        self.name = name
        self.email = email
        self.enquiry = enquiry

    @staticmethod
    def random():
        name = fake.first_name()
        email = fake.email()
        enquiry = fake.words(15)
        return ContactUsData(name, email, enquiry,)
