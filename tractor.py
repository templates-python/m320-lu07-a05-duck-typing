from vehicle import Vehicle

class Tractor(Vehicle):

    def __init__(self, inventory, designation):
        super().__init__('Traktor', inventory, designation)