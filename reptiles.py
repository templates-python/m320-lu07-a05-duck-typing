from animals import Animal


class Reptil(Animal):

    def __init__(self, species, name, inventory):
        super().__init__('Reptil', species, inventory, name)
