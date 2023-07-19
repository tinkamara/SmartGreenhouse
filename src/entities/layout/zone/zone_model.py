from src.entities.devices.fan.fan_model import FanModel
from src.entities.devices.fertilizer.fertilizer_model import FertilizerModel
from src.entities.devices.heater.heater_model import Heater
from src.entities.devices.irrigation.irrigation_model import Irrigation
from src.entities.devices.lamp.lamp_model import Lamp
from src.entities.devices.uv_lamp.uv_lamp_model import UVLampModel
from src.entities.devices.water_dispenser.water_dispenser_model import WaterDispenser
from src.entities.sensors.air_humidity_sensor import AirHumiditySensor
from src.entities.sensors.soil_humidity_sensor import SoilHumiditySensor
from src.entities.sensors.thermometer import Thermometer


class ZoneModel:

    def __init__(self, plant: str, ideal_temperature: int, ideal_air_humidity: int, ideal_soil_humidity: int, thermometer: Thermometer, soil_humidity_sensor: SoilHumiditySensor, air_humidity_sensor: AirHumiditySensor,
                 heater: Heater, fan: FanModel, fertilizer: FertilizerModel, irrigation: Irrigation, lamp: Lamp, uv_lamp: UVLampModel, water_dispenser: WaterDispenser):

        self.plant = plant
        self.ideal_temperature = ideal_temperature
        self.ideal_air_humidity: int = ideal_air_humidity
        self.ideal_soil_humidity: int = ideal_soil_humidity
        self.thermometer: Thermometer = thermometer
        self.soil_humidity_sensor: SoilHumiditySensor = soil_humidity_sensor
        self.air_humidity_sensor: AirHumiditySensor = air_humidity_sensor
        self.heater: Heater = heater
        self.fan: FanModel = fan
        self.fertilizer: FertilizerModel = fertilizer
        self.irrigation: Irrigation = irrigation
        self.lamp: Lamp = lamp
        self.uv_lamp: UVLampModel = uv_lamp
        self.water_dispenser: WaterDispenser = water_dispenser

