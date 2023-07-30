import unittest
from unittest.mock import Mock

from src.entities.devices.fertilizer.fertilizer_model import FertilizerModel
from src.entities.devices.irrigation.irrigation_model import IrrigationModel
from src.entities.devices.uv_lamp.uv_lamp_model import UVLampModel
from src.entities.layout.plant.plant_model import PlantModel
from src.entities.layout.zone.zone_model import ZoneModel
from src.entities.sensors.soil_humidity_sensor import SoilHumiditySensor


class TestPlantModel(unittest.TestCase):

    def setUp(self):
        # Erstelle Mock-Objekte für die Abhängigkeiten der PlantModel-Klasse
        self.zone_mock = Mock(spec=ZoneModel)
        self.soil_humidity_sensor_mock = Mock(spec=SoilHumiditySensor)
        self.fertilizer_mock = Mock(spec=FertilizerModel)
        self.irrigation_mock = Mock(spec=IrrigationModel)
        self.uv_lamp_mock = Mock(spec=UVLampModel)

        # Erstelle eine Instanz der PlantModel-Klasse für jeden Testfall
        self.plant = PlantModel("Testpflanze", self.zone_mock, 60, self.soil_humidity_sensor_mock,
                                self.fertilizer_mock, self.irrigation_mock, self.uv_lamp_mock)

    def test_initial_values(self):
        # Teste, ob die Attribute beim Initialisieren korrekt gesetzt werden
        self.assertEqual(self.plant.name, "Testpflanze")
        self.assertIs(self.plant.zone, self.zone_mock)
        self.assertIs(self.plant.uv_lamp, self.uv_lamp_mock)
        self.assertIs(self.plant.fertilizer, self.fertilizer_mock)
        self.assertIs(self.plant.irrigation, self.irrigation_mock)
        self.assertIs(self.plant.soil_humidity_sensor, self.soil_humidity_sensor_mock)
        self.assertEqual(self.plant.ideal_soil_humidity, 60)

    def test_increase_ideal_soil_humidity(self):
        # Teste, ob die Methode zur Erhöhung der idealen Bodenfeuchtigkeit richtig funktioniert
        self.plant.increase_ideal_soil_humidity(10)
        self.assertEqual(self.plant.ideal_soil_humidity, 70)

    def test_decrease_ideal_soil_humidity(self):
        # Teste, ob die Methode zur Verringerung der idealen Bodenfeuchtigkeit richtig funktioniert
        self.plant.decrease_ideal_soil_humidity(20)
        self.assertEqual(self.plant.ideal_soil_humidity, 40)