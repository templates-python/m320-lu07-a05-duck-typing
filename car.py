from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, inventory, designation):
        super().__init__('Auto', inventory, designation)