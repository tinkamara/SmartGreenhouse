from src.entities.abstract.device.device_model import DeviceModel
from src.entities.layout.greenhouse.greenhouse_model import GreenhouseModel
from src.exceptions.not_enough_water_in_tank_Exception import NotEnoughWaterInTankException
from src.utilities.log import Log


class IrrigationModel(DeviceModel):

    def __init__(self):
        greenhouse = GreenhouseModel()
        self.water_tank = greenhouse.water_tank
        self.name = "Bewässerung"
        self.type = "Water"

    def water_plant(self):
        try:
            self.water_tank.take_water(1)
        except NotEnoughWaterInTankException as e:
            Log.write_to_log(e.message, 1)

