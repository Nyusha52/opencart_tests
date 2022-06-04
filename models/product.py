from faker import Faker

fake = Faker("Ru-ru")


class ProductData:
    def __init__(self, name=None, meta_tag=None, model=None):
        self.name = name
        self.meta_tag = meta_tag
        self.model = model

    @staticmethod
    def random():
        name = fake.word()
        meta_tag = fake.word()
        model = fake.word()
        return ProductData(name, meta_tag, model)
