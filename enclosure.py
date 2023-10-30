from building import Building


class Enclosure(Building):

    def __init__(self, inventory, designation):
        super().__init__('Gehege', inventory, designation)
