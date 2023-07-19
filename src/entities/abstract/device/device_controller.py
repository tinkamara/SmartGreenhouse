from abc import ABC, abstractmethod


class DeviceController(ABC):

    @abstractmethod
    def __init__(self, model, view):
        pass

    @abstractmethod
    def update_view(self):
        pass
