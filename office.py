from building import Building

class Office(Building):

    def __init__(self, inventory, designation):
        super().__init__('Büro', inventory, designation)