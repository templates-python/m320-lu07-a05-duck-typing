from animals import Animal


class Mammals(Animal):

    def __init__(self, species, inventory, name):
        super().__init__('Säugetier', species, inventory, name)
