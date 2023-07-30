from src.entities.devices.lamp.lamp_model import Lamp
from src.entities.devices.water_tank.water_tank_model import WaterTank
from src.entities.layout.zone.zone_model import ZoneModel


class GreenhouseModel:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.zones: [ZoneModel] = []
        self.main_light = Lamp()
        self.water_tank = WaterTank()


