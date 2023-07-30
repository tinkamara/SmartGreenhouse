import unittest

from src.entities.devices.water_tank.water_tank_model import WaterTank
from src.exceptions.not_enough_water_in_tank_Exception import NotEnoughWaterInTankException


class TestWaterTank(unittest.TestCase):

    def setUp(self):
        self.water_tank = WaterTank()

    def test_take_water_success(self):
        # Testen, ob das Entnehmen von Wasser erfolgreich ist
        initial_water_level = self.water_tank.get_water_level()
        self.water_tank.take_water(10)
        self.assertEqual(self.water_tank.get_water_level(), initial_water_level - 10)

    def test_take_water_not_enough_water(self):
        # Testen, ob eine Ausnahme ausgelöst wird, wenn nicht genügend Wasser im Behälter ist
        initial_water_level = self.water_tank.get_water_level()
        with self.assertRaises(NotEnoughWaterInTankException):
            self.water_tank.take_water(initial_water_level + 10)

    def test_add_water(self):
        # Testen, ob das Hinzufügen von Wasser erfolgreich ist
        initial_water_level = self.water_tank.get_water_level()
        self.water_tank.add_water(20)
        self.assertEqual(self.water_tank.get_water_level(), initial_water_level + 20)

    def test_get_water_level(self):
        # Testen, ob die Methode get_water_level den richtigen Wasserstand zurückgibt
        self.assertEqual(self.water_tank.get_water_level(), 50)