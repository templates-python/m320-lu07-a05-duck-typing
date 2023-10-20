from abc import ABC
class Animal(ABC):

    def __init__(self, genus, species, inventory, name):
        self._genus = genus
        self._species = species
        self._inventory = inventory
        self._name = name


    @property
    def species(self):
        return self._species

    @property
    def genus(self):
        return self._genus

    @property
    def name(self):
        return self._name

    @property
    def inventory(self):
        return self._inventory

    def __str__(self):
        return f'{self._genus}: {self._species}: {self._name}  -- {self._inventory}'

