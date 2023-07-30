import unittest
from unittest.mock import MagicMock
from src.entities.sensors.air_humidity_sensor import AirHumiditySensor

class TestAirHumiditySensor(unittest.TestCase):

    def setUp(self):
        self.air_humidity_sensor = AirHumiditySensor()

    def test_initial_air_humidity_value(self):
        self.assertEqual(self.air_humidity_sensor.get_value(), 25)

    def test_lower_value(self):
        self.air_humidity_sensor.lower_value(5)
        self.assertEqual(self.air_humidity_sensor.get_value(), 20)

    def test_raise_value(self):
        self.air_humidity_sensor.raise_value(10)
        self.assertEqual(self.air_humidity_sensor.get_value(), 35)

    def test_random_value_change(self):
        # Mock the random function to return 2 (for testing raise_value)
        with unittest.mock.patch('random.choice', return_value=2):
            self.air_humidity_sensor.random_value_change()
        self.assertEqual(self.air_humidity_sensor.get_value(), 27)

        # Mock the random function to return -2 (for testing lower_value)
        with unittest.mock.patch('random.choice', return_value=-2):
            self.air_humidity_sensor.random_value_change()
        self.assertEqual(self.air_humidity_sensor.get_value(), 25)

    def test_random_value_change_with_actual_random(self):
        # Test random_value_change with actual random values (not mocked)
        original_value = self.air_humidity_sensor.get_value()
        self.air_humidity_sensor.random_value_change()
        new_value = self.air_humidity_sensor.get_value()
        self.assertTrue(new_value in range(original_value - 2, original_value + 3))