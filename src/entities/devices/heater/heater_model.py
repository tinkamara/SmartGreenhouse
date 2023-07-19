
from src.entities.abstract.binary_device.binary_device_model import BinaryDeviceModel
from src.entities.abstract.scalable_device.scalable_device_model import ScalableDeviceModel


class HeaterModel(ScalableDeviceModel, BinaryDeviceModel):

    def __init__(self):
        self.is_on: bool = False
        self.power: int = 50

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def scale_device(self, value):
        self.power += value

        if self.power > 100:
            self.power = 100
        elif self.power < 0:
            self.power = 0



