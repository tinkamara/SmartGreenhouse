
from src.entities.abstract.binary_device.binary_device_model import BinaryDeviceModel
from src.entities.abstract.scalable_device.scalable_device_model import ScalableDeviceModel
from src.utilities.log import Log


class UVLampModel(ScalableDeviceModel):

    def __init__(self):
        self.brightness = 0
        self.name = "UV-Licht"
        self.type = "UV"

    def scale_device(self, value):
        self.brightness += value
        if self.brightness > 100:
            self.brightness = 100
        elif self.brightness < 0:
            self.brightness = 0
        Log.write_to_log('UV-Lampe auf ' + str(self.brightness) + '% eingestellt', 1)

