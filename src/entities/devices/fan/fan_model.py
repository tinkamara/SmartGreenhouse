from src.entities.abstract.scalable_device.scalable_device_model import ScalableDeviceModel
from src.utilities.log import Log


class FanModel(ScalableDeviceModel):

    def __init__(self):
        self.name = "Lüfter"
        self.type = "LF"
        self.power = 50

    def scale_device(self, value):
        self.power += value
        if self.power > 100:
            self.power = 100
        elif self.power < 0:
            self.power = 0

