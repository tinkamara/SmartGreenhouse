from abc import abstractmethod

from src.entities.abstract.device.device_model import DeviceModel


class ScalableDeviceModel(DeviceModel):

    @abstractmethod
    def scale_device(self, value):
        pass
