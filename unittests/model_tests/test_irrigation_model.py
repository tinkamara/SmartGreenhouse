import unittest
from unittest.mock import Mock

from src.entities.devices.irrigation.irrigation_model import IrrigationModel
from src.exceptions.not_enough_water_in_tank_Exception import NotEnoughWaterInTankException


class TestIrrigationModel(unittest.TestCase):

    def test_water_plant_with_enough_water(self):
        # Erstellen eines Mock-Objekts für den water_tank
        mock_water_tank = Mock()
        mock_water_tank.take_water.return_value = 1

        irrigation = IrrigationModel()
        irrigation.water_tank = mock_water_tank  # Ersetzen des water_tank-Attributs durch den Mock

        irrigation.water_plant()

        # Überprüfen, ob die take_water-Methode einmal aufgerufen wurde
        mock_water_tank.take_water.assert_called_once_with(1)


    def test_water_plant_with_not_enough_water(self):
        # Erstellen eines Mock-Objekts für den water_tank
        mock_water_tank = Mock()
        mock_water_tank.take_water.side_effect = NotEnoughWaterInTankException()

        irrigation = IrrigationModel()
        irrigation.water_tank = mock_water_tank  # Ersetzen des water_tank-Attributs durch den Mock

        irrigation.water_plant()

        # Überprüfen, ob die take_water-Methode einmal aufgerufen wurde
        mock_water_tank.take_water.assert_called_once_with(1)
