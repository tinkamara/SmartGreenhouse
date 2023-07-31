from src.entities.devices.fan.fan_model import FanModel
from src.entities.devices.heater.heater_model import HeaterModel
from src.entities.devices.lamp.lamp_model import Lamp
from src.entities.devices.television.television_model import TelevisionModel
from src.entities.devices.water_dispenser.water_dispenser_model import WaterDispenserModel
from src.entities.sensors.air_humidity_sensor import AirHumiditySensor
from src.entities.sensors.thermometer import Thermometer


class RoomModel:

    def __init__(self, name: str, ideal_temperature: int, ideal_air_humidity: int, thermometer: Thermometer, air_humidity_sensor: AirHumiditySensor,
                 heater: HeaterModel, fan: FanModel, lamp: Lamp, water_dispenser: WaterDispenserModel, television: TelevisionModel, devices: []):
        self.name = name
        self.ideal_temperature = ideal_temperature
        self.ideal_air_humidity: int = ideal_air_humidity
        self.thermometer: Thermometer = thermometer
        self.air_humidity_sensor: AirHumiditySensor = air_humidity_sensor
        self.heater: HeaterModel = heater
        self.fan: FanModel = fan
        self.lamp: Lamp = lamp
        self.water_dispenser: WaterDispenserModel = water_dispenser
        self.television: TelevisionModel = television
        self.devices = devices

    def increase_ideal_temperature(self, increment: int):
        self.ideal_temperature += increment

        # Methode zum Verringern der idealen Temperatur um einen bestimmten Wert

    def decrease_ideal_temperature(self, decrement: int):
        self.ideal_temperature -= decrement

        # Methode zum Erhöhen der idealen Luftfeuchtigkeit um einen bestimmten Wert

    def increase_ideal_air_humidity(self, increment: int):
        self.ideal_air_humidity += increment

        # Methode zum Verringern der idealen Luftfeuchtigkeit um einen bestimmten Wert
    def decrease_ideal_air_humidity(self, decrement: int):
        self.ideal_air_humidity -= decrement


