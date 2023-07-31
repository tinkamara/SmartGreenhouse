from src.entities.abstract.binary_device.binary_device_model import BinaryDeviceModel
from src.entities.abstract.scalable_device.scalable_device_model import ScalableDeviceModel
from src.utilities.log import Log


class HeaterModel(ScalableDeviceModel):

    def __init__(self):
        self.power: int = 50
        self.name = "Heizung"
        self.type = "HZ"

    def scale_device(self, value):
        self.power += value

        if self.power > 100:
            self.power = 100
        elif self.power < 0:
            self.power = 0
