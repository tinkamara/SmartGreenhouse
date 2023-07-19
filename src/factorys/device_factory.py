import threading

from src.entities.abstract.device.device import Device
from src.entities.devices.uv_lamp.uv_lamp_controller import UVLampController
from src.entities.devices.uv_lamp.uv_lamp_model import UVLampModel
from src.entities.devices.uv_lamp.uv_lamp_view import UVLampView


class DeviceFactory:
    def __init__(self):
        self.devices = []

    def create_uv_lamp(self):
        uv_lamp_model = UVLampModel()
        uv_lamp_view = UVLampView(uv_lamp_model)
        uv_lamp_controller = UVLampController(uv_lamp_model, uv_lamp_view)
        uv_lamp = Device(uv_lamp_model, uv_lamp_view, uv_lamp_controller)
        self.devices.append(uv_lamp)
        return uv_lamp

