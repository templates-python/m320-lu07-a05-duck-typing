from car import Car
from tractor import Tractor
from catering import Catering
from office import Office
from enclosure import Enclosure
from cobra import Cobra
from crocodile import Crocodile
from wolf import  Wolf
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




