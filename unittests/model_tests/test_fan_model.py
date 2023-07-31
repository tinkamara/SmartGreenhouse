import unittest

from src.entities.devices.fan.fan_model import FanModel


class TestFanModel(unittest.TestCase):

    def test_scale_device_within_range(self):
        fan = FanModel()

        fan.scale_device(50)
        self.assertEqual(fan.power, 100)  # Überprüfen, ob die Leistung korrekt gesetzt wurde

        fan.scale_device(75)
        self.assertEqual(fan.power, 100)  # Überprüfen, ob die Leistung korrekt gesetzt wurde

    def test_scale_device_above_100(self):
        fan = FanModel()

        fan.scale_device(120)
        self.assertEqual(fan.power, 100)  # Überprüfen, ob die Leistung auf 100 begrenzt wurde

    def test_scale_device_below_0(self):
        fan = FanModel()

        fan.scale_device(-50)
        self.assertEqual(fan.power, 0) # Überprüfen, ob die Leistung auf 0 begrenzt wurde