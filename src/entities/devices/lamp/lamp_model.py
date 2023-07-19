from src.abstract_model.binary_device_model import BinaryDevice


class Lamp(BinaryDevice):

    def __init__(self):
        self.status = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
