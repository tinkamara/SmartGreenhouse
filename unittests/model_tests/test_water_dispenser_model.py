import unittest
from unittest import mock
from unittest.mock import Mock, patch
from src.entities.devices.water_dispenser.water_dispenser_model import WaterDispenserModel
from src.exceptions.not_enough_water_in_tank_Exception import NotEnoughWaterInTankException
from src.utilities.log import Log


class TestWaterDispenserModel(unittest.TestCase):

    @patch('src.entities.layout.greenhouse.greenhouse_model.GreenhouseModel')
    def setUp(self, mock_greenhouse_model):
        self.water_tank_mock = Mock()
        mock_greenhouse_model.return_value.water_tank = self.water_tank_mock
        self.water_dispenser = WaterDispenserModel()
        self.log_mock = mock.MagicMock()
        Log.write_to_log = self.log_mock

    def test_dispense_water_successful(self):
        self.water_dispenser.dispense_water()
        self.water_tank_mock.take_water.assert_called_once_with(1)
        Log.write_to_log.assert_called_once_with("Wasser aus der Regentonne entnommen.", 1)

