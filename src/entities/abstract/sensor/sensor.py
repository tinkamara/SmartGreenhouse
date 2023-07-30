from abc import abstractmethod

from src.entities.abstract.device.device_model import DeviceModel


class Sensor(DeviceModel):

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def lower_value(self, value):
        pass

    @abstractmethod
    def raise_value(self, value):
        pass

    @abstractmethod
    def random_value_change(self):
        pass
