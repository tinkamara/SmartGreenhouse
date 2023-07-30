import unittest
from src.entities.layout.greenhouse.greenhouse_model import GreenhouseModel
from src.entities.layout.zone.zone_model import ZoneModel
from src.entities.devices.lamp.lamp_model import Lamp
from src.entities.devices.water_tank.water_tank_model import WaterTank

class TestGreenhouseModel(unittest.TestCase):

    def setUp(self):
        self.greenhouse = GreenhouseModel()

    def test_singleton_instance(self):
        # Teste, ob GreenhouseModel eine Singleton-Klasse ist
        greenhouse1 = GreenhouseModel()
        greenhouse2 = GreenhouseModel()
        self.assertIs(greenhouse1, greenhouse2)

    def test_add_zone(self):
        zone = ZoneModel(name="Test Zone",
                         ideal_temperature=25, ideal_air_humidity=50,
                         thermometer=None, air_humidity_sensor=None,
                         heater=None, fan=None, lamp=None, water_dispenser=None)

        self.greenhouse.zones.append(zone)
        self.assertIn(zone, self.greenhouse.zones)

    def test_main_light_instance(self):
        self.assertIsInstance(self.greenhouse.main_light, Lamp)

    def test_water_tank_instance(self):
        self.assertIsInstance(self.greenhouse.water_tank, WaterTank)