from src.entities.abstract.binary_device.binary_device_model import BinaryDeviceModel
from src.utilities.log import Log


class Lamp(BinaryDeviceModel):

    def __init__(self):
        self.is_on = False
        self.name = "Lampe"
        self.type = "Light"

    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False

