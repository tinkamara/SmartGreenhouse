from src.entities.devices.uv_lamp.uv_lamp_model import UVLampModel
from src.entities.devices.uv_lamp.uv_lamp_view import UVLampView
from src.factorys.device_factory import DeviceFactory

if __name__ == "__main__":

    device_factory = DeviceFactory()
    uv_lamp = device_factory.create_uv_lamp()
    device_factory.start_threads()
    uvlamp = uv_lamp.model
    view = uv_lamp.view


