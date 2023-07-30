import unittest

from src.entities.devices.heater.heater_model import HeaterModel


class TestHeaterModel(unittest.TestCase):

    def test_initial_power(self):
        heater = HeaterModel()

        self.assertEqual(heater.power, 50)  # Überprüfen, ob die Leistung zu Beginn 50 ist

    def test_scale_device_increase(self):
        heater = HeaterModel()

        heater.scale_device(30)
        self.assertEqual(heater.power, 80)  # Überprüfen, ob die Leistung um 30 erhöht wurde (50 + 30 = 80)

        heater.scale_device(50)
        self.assertEqual(heater.power, 100)  # Überprüfen, ob die Leistung den Maximalwert 100 nicht überschreitet

    def test_scale_device_decrease(self):
        heater = HeaterModel()

        heater.scale_device(-20)
        self.assertEqual(heater.power, 30)  # Überprüfen, ob die Leistung um 20 verringert wurde (50 - 20 = 30)

        heater.scale_device(-40)
        self.assertEqual(heater.power, 0)  # Überprüfen, ob die Leistung den Minimalwert 0 nicht unterschreitet

    def test_scale_device_invalid_values(self):
        heater = HeaterModel()

        heater.scale_device(200)
        self.assertEqual(heater.power, 100)  # Überprüfen, ob die Leistung den Maximalwert 100 nicht überschreitet

        heater.scale_device(-100)
        self.assertEqual(heater.power, 0)  # Überprüfen, ob die Leistung den Minimalwert 0 nicht unterschreitet
