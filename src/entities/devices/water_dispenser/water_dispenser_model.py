from src.entities.abstract.device.device_model import DeviceModel

from src.exceptions.not_enough_water_in_tank_Exception import NotEnoughWaterInTankException
from src.utilities.log import Log


class WaterDispenserModel(DeviceModel):

    def __init__(self):
        from src.entities.layout.greenhouse.greenhouse_model import GreenhouseModel
        greenhouse = GreenhouseModel()
        self.water_tank = greenhouse.water_tank
        self.name = "Luftbefeuchter"
        self.type = "Luft"

    def dispense_water(self):
        try:
            self.water_tank.take_water(1)
            Log.write_to_log("Wasser aus der Regentonne entnommen.", 1)
        except NotEnoughWaterInTankException as e:
            Log.write_to_log(e.message, 1)
