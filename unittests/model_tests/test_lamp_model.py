import unittest

from src.entities.devices.lamp.lamp_model import Lamp


class TestLamp(unittest.TestCase):

    def test_turn_on(self):
        lamp = Lamp()
        lamp.turn_on()
        self.assertTrue(lamp.is_on)  # Überprüfen, ob die Lampe eingeschaltet ist


    def test_turn_off(self):
        lamp = Lamp()
        lamp.turn_on()  # Schalten Sie die Lampe zuerst ein, um sicherzustellen, dass sie ausgeschaltet werden kann
        lamp.turn_off()
        self.assertFalse(lamp.is_on)  # Überprüfen, ob die Lampe ausgeschaltet ist
