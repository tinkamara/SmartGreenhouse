
from src.entities.abstract.binary_device.binary_device_model import BinaryDeviceModel
from src.entities.abstract.scalable_device.scalable_device_model import ScalableDeviceModel


class UVLampModel(ScalableDeviceModel, BinaryDeviceModel):

    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def scale_device(self, value):
        self.brightness = value
        if self.brightness > 100:
            self.brightness = 100
        elif self.brightness < 0:
            self.brightness = 0

