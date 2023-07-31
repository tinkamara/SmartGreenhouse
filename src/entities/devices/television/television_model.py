
from src.entities.abstract.binary_device.binary_device_model import BinaryDeviceModel
from src.entities.abstract.scalable_device.scalable_device_model import ScalableDeviceModel
from src.utilities.log import Log


class TelevisionModel(BinaryDeviceModel, ScalableDeviceModel):

    def __init__(self):
        self.name = "Fernseher"
        self.type = "TV"
        self.is_on = False
        self.volume = 0

    def scale_device(self, value):
        self.volume = value
        if self.volume > 100:
            self.volume = 100
        elif self.volume < 0:
            self.volume = 0


    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False
