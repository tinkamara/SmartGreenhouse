import unittest
from unittest.mock import Mock

from src.entities.devices.fan.fan_model import FanModel
from src.entities.devices.heater.heater_model import HeaterModel
from src.entities.devices.lamp.lamp_model import Lamp
from src.entities.devices.water_dispenser.water_dispenser_model import WaterDispenserModel
from src.entities.layout.zone.zone_model import ZoneModel
from src.entities.sensors.air_humidity_sensor import AirHumiditySensor
from src.entities.sensors.thermometer import Thermometer


class TestZoneModel(unittest.TestCase):

    def setUp(self):
        # Erstelle Mock-Objekte für die Abhängigkeiten der ZoneModel-Klasse
        self.thermometer_mock = Mock(spec=Thermometer)
        self.air_humidity_sensor_mock = Mock(spec=AirHumiditySensor)
        self.heater_mock = Mock(spec=HeaterModel)
        self.fan_mock = Mock(spec=FanModel)
        self.lamp_mock = Mock(spec=Lamp)
        self.water_dispenser_mock = Mock(spec=WaterDispenserModel)
        self.devices = []

        # Erstelle eine Instanz der ZoneModel-Klasse für jeden Testfall
        self.zone = ZoneModel("Testzone", 25, 60, self.thermometer_mock,
                              self.air_humidity_sensor_mock, self.heater_mock, self.fan_mock,
                              self.lamp_mock, self.water_dispenser_mock, self.devices)

    def test_initial_values(self):
        # Teste, ob die Attribute beim Initialisieren korrekt gesetzt werden
        self.assertEqual(self.zone.name, "Testzone")
        self.assertEqual(self.zone.ideal_temperature, 25)
        self.assertEqual(self.zone.ideal_air_humidity, 60)
        self.assertIs(self.zone.thermometer, self.thermometer_mock)
        self.assertIs(self.zone.air_humidity_sensor, self.air_humidity_sensor_mock)
        self.assertIs(self.zone.heater, self.heater_mock)
        self.assertIs(self.zone.fan, self.fan_mock)
        self.assertIs(self.zone.lamp, self.lamp_mock)
        self.assertIs(self.zone.water_dispenser, self.water_dispenser_mock)

    def test_increase_ideal_temperature(self):
        # Teste, ob die Methode zur Erhöhung der idealen Temperatur richtig funktioniert
        self.zone.increase_ideal_temperature(5)
        self.assertEqual(self.zone.ideal_temperature, 30)

    def test_decrease_ideal_temperature(self):
        # Teste, ob die Methode zur Verringerung der idealen Temperatur richtig funktioniert
        self.zone.decrease_ideal_temperature(10)
        self.assertEqual(self.zone.ideal_temperature, 15)

    def test_increase_ideal_air_humidity(self):
        # Teste, ob die Methode zur Erhöhung der idealen Luftfeuchtigkeit richtig funktioniert
        self.zone.increase_ideal_air_humidity(15)
        self.assertEqual(self.zone.ideal_air_humidity, 75)

    def test_decrease_ideal_air_humidity(self):
        # Teste, ob die Methode zur Verringerung der idealen Luftfeuchtigkeit richtig funktioniert
        self.zone.decrease_ideal_air_humidity(20)
        self.assertEqual(self.zone.ideal_air_humidity, 40)