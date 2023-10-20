from abc import ABC
class Vehicle(ABC):

    def __init__(self, kind_of, inventory, designation):
        self._kind_of = kind_of
        self._inventory = inventory
        self._designation = designation

    @property
    def kind_of(self):
        return self._kind_of

    @property
    def designation(self):
        return self._designation

    @property
    def inventory(self):
        return self._inventory

    def __str__(self):
        return f'{self._kind_of}: {self._designation}  -- {self._inventory}'