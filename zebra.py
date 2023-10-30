from mammals import Mammals


class Zebra(Mammals):

    def __init__(self, name, inventory):
        super().__init__('Zebra', 7000.0, name)
