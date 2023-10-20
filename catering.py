from building import Building
class Catering(Building):

    def __init__(self, inventory, designation):
        super().__init__('Verpflegung', inventory, designation)