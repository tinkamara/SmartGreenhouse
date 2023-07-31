from src.entities.devices.fan.fan_model import FanModel
from src.entities.devices.heater.heater_model import HeaterModel
from src.entities.devices.lamp.lamp_model import Lamp
from src.entities.devices.water_dispenser.water_dispenser_model import WaterDispenserModel
from src.entities.layout.zone.zone_controller import ZoneController
from src.entities.layout.zone.zone_model import ZoneModel
from src.entities.sensors.air_humidity_sensor import AirHumiditySensor
from src.entities.sensors.thermometer import Thermometer


class ZoneFactory:

    @staticmethod
    def create_zone(name: str, ideal_temperature: int, ideal_air_humidity: int):
        thermometer: Thermometer = Thermometer()
        air_humidity_sensor: AirHumiditySensor = AirHumiditySensor()
        heater: HeaterModel = HeaterModel()
        fan: FanModel = FanModel()
        lamp: Lamp = Lamp()
        water_dispenser: WaterDispenserModel = WaterDispenserModel()
        devices = [heater, fan, lamp, water_dispenser]

        zone_model = ZoneModel(name, ideal_temperature, ideal_air_humidity, thermometer, air_humidity_sensor,
                               heater, fan, lamp, water_dispenser, devices)
        zone_controller = ZoneController(zone_model)
        zone_controller.start()
        return zone_controller
