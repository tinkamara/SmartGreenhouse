from src.abstract_model.device_model import Device

from src.entities.abstract.device.device_model import DeviceModel
from src.exceptions.not_enough_water_in_tank_Exception import NotEnoughWaterInTankException
from utilities.log import Log


class IrrigationModel(DeviceModel):

    def __init__(self, water_tank):
        self.water_tank: WaterTank = water_tank

    def water_plant(self):
        try:
            self.water_tank.take_water(1)
            Log.write_to_log("Wasser aus der Regentonne entnommen.", 1)
        except NotEnoughWaterInTankException as e:
            Log.write_to_log(e.message, 1)

