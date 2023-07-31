import threading
import time

from src.entities.layout.zone.zone_model import ZoneModel
from src.factorys.plant_factory import PlantFactory
from src.utilities.log import Log


class ZoneController:
    controllers = []

    @staticmethod
    def get_zone_controller_by_name(zone_name):
        for index, zone_controller in enumerate(ZoneController.controllers):
            if zone_controller.zone_model.name == zone_name:
                return zone_controller

    def __init__(self, zone_model: ZoneModel):
        self.zone_model: ZoneModel = zone_model
        self.running = False
        self.thread = None
        ZoneController.controllers.append(self)

    def control_devices(self):
        while self.running:

            current_temperature = self.zone_model.thermometer.get_value()
            current_air_humidity = self.zone_model.air_humidity_sensor.get_value()


            if current_temperature < self.zone_model.ideal_temperature:
                self.zone_model.heater.scale_device(10)
                self.zone_model.thermometer.raise_value(1)
                Log.write_to_log("Heizung in " + str(self.zone_model.name) + " auf " + str(
                    self.zone_model.heater.power) + "% erhoeht", 1)
            else:
                self.zone_model.heater.scale_device(-100)
                Log.write_to_log(
                    "Heizung in " + str(self.zone_model.name) + " ausgeschaltet",
                    1)

            if current_temperature > self.zone_model.ideal_temperature:
                self.zone_model.fan.scale_device(10)
                self.zone_model.thermometer.lower_value(1)
                self.zone_model.air_humidity_sensor.lower_value(1)
                Log.write_to_log(
                    "Luefter in " + str(self.zone_model.name) + " auf " + str(self.zone_model.fan.power) + "% erhoeht",
                    1)
            else:
                self.zone_model.heater.scale_device(-100)
                Log.write_to_log("Luefter in " + str(self.zone_model.name) + " ausgeschaltet",
                1)

            if current_air_humidity < self.zone_model.ideal_air_humidity:
                self.zone_model.water_dispenser.dispense_water()
                self.zone_model.air_humidity_sensor.raise_value(5)
                Log.write_to_log("Wasser in " + str(self.zone_model.name) + " versprueht", 1)

            self.zone_model.air_humidity_sensor.random_value_change()
            time.sleep(10)

    def add_plant(self, name, type: str, i_soil_humidity, uv_lamp_scale):
        plant_controller = PlantFactory.create_plant(name, type, self.zone_model, i_soil_humidity, uv_lamp_scale)
        self.zone_model.plants.append(plant_controller.plant_model)

    def remove_plant(self, plant_name):
        value_to_remove = plant_name
        index_to_remove = None
        for index, obj in enumerate(self.zone_model.plants):
            if obj.name == value_to_remove:
                index_to_remove = index

        if index_to_remove is not None:
            self.zone_model.plants.pop(index_to_remove)


    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.control_devices)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()
            self.thread = None
