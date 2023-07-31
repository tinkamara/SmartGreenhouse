from src.entities.devices.fan.fan_model import FanModel
from src.entities.devices.heater.heater_model import HeaterModel
from src.entities.devices.lamp.lamp_model import Lamp
from src.entities.devices.television.television_model import TelevisionModel
from src.entities.devices.water_dispenser.water_dispenser_model import WaterDispenserModel
from src.entities.layout.room.room_controller import RoomController
from src.entities.layout.room.room_model import RoomModel
from src.entities.sensors.air_humidity_sensor import AirHumiditySensor
from src.entities.sensors.thermometer import Thermometer


class RoomFactory:

    @staticmethod
    def create_room(name: str, ideal_temperature: int, ideal_air_humidity: int):
        thermometer: Thermometer = Thermometer()
        air_humidity_sensor: AirHumiditySensor = AirHumiditySensor()
        heater: HeaterModel = HeaterModel()
        fan: FanModel = FanModel()
        lamp: Lamp = Lamp()
        water_dispenser: WaterDispenserModel = WaterDispenserModel()
        television: TelevisionModel = TelevisionModel()
        devices = [heater, fan, lamp, water_dispenser, television]

        room_model = RoomModel(name, ideal_temperature, ideal_air_humidity, thermometer, air_humidity_sensor,
                 heater, fan, lamp, water_dispenser, television, devices)
        room_controller = RoomController(room_model)
        room_controller.start()
        return room_controller

