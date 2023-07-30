import unittest

from src.entities.devices.uv_lamp.uv_lamp_model import UVLampModel


class TestUVLampModel(unittest.TestCase):

    def test_scale_device(self):
        lamp = UVLampModel()

        # Test, ob die Helligkeit korrekt skaliert wird, wenn der Wert innerhalb des gültigen Bereichs liegt
        lamp.scale_device(50)
        self.assertEqual(lamp.brightness, 50)

        # Test, ob die Helligkeit auf den maximalen Wert (100) begrenzt wird
        lamp.scale_device(200)
        self.assertEqual(lamp.brightness, 100)

        # Test, ob die Helligkeit auf den minimalen Wert (0) begrenzt wird
        lamp.scale_device(-100)
        self.assertEqual(lamp.brightness, 0)

