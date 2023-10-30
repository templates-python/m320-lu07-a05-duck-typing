from mammals import Mammals


class Wolf(Mammals):

    def __init__(self, name, inventory):
        super().__init__('Wolf', 2000.0, name)
