from car import Car
from catering import Catering
from cobra import Cobra
from crocodile import Crocodile
from enclosure import Enclosure
from office import Office
from tractor import Tractor
from wolf import Wolf
from zebra import Zebra


class Zoo:

    def __init__(self):
        self._buildings = []
        self._vehicles = []
        self._animals = []
        self.create_buildings()
        self.create_vehicles()
        self.buy_animals()

    def create_buildings(self):
        self._buildings.append(Office(250000.0, 'Verwaltung'))
        self._buildings.append(Office(100000.0, 'Krankenstation'))
        self._buildings.append(Catering(500000.0, 'Restaurant'))
        self._buildings.append(Catering(30000.0, 'Kiosk'))
        self._buildings.append(Enclosure(1000000.0, 'Wolfsgrube'))
        self._buildings.append(Enclosure(240000.0, 'Steppe'))
        self._buildings.append(Enclosure(750000.0, 'Reptilienhaus'))
        self._buildings.append(Enclosure(330000.0, 'Amazonas'))

    def create_vehicles(self):
        self._vehicles.append(Car(75000.0, 'CEO'))
        self._vehicles.append(Car(25000.0, 'Tierarzt'))
        self._vehicles.append(Tractor(200000.0, 'Unterhalt'))

    def buy_animals(self):
        self._animals.append(Wolf(10000.0, 'Luna'))
        self._animals.append(Wolf(10000.0, 'Odin'))
        self._animals.append(Wolf(10000.0, 'Yukon'))
        self._animals.append(Wolf(10000.0, 'Nala'))
        self._animals.append(Zebra(33000.0, 'Ziggy'))
        self._animals.append(Zebra(33000.0, 'Zeena'))
        self._animals.append(Zebra(33000.0, 'Zebedee'))
        self._animals.append(Zebra(33000.0, 'Zephyra'))
        self._animals.append(Zebra(33000.0, 'Zia'))
        self._animals.append(Crocodile(52000.0, 'Snapper'))
        self._animals.append(Crocodile(52000.0, 'Crocstar'))
        self._animals.append(Cobra(7000.0, 'Medusa'))

    def print_all_buildings(self):
        print(f'----\nAnzahl Gebäude: {len(self._buildings)}')
        for building in self._buildings:
            print(building)

    def print_all_vehicles(self):
        print(f'----\nAnzahl Verkehrsmittel: {len(self._vehicles)}')
        for vehicle in self._vehicles:
            print(vehicle)

    def print_all_animals(self):
        print(f'----\nAnzahl Tiere: {len(self._animals)}')
        for animal in self._animals:
            print(animal)

    def print_worth_of_the_zoo(self):
        inventory_elements = self._animals + self._vehicles + self._buildings
        print(f'---\n{len(inventory_elements)} Objekte im Inventar mit Totalwert von')
        worth = 0.0
        for element in inventory_elements:
            if hasattr(element, 'inventory'):
                worth += element.inventory
        print(f'Fr. {worth}')
