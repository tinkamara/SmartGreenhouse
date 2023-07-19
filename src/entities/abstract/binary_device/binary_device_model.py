from abc import abstractmethod

from src.entities.abstract.device.device_model import DeviceModel


class BinaryDeviceModel(DeviceModel):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass
