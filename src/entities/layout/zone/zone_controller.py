import threading
import time

from src.entities.layout.zone.zone_model import ZoneModel
from src.factorys.plant_factory import PlantFactory


class ZoneController:

    def __init__(self, zone_model: ZoneModel):
        self.zone_model: ZoneModel = zone_model
        self.running = False
        self.thread = None

    def control_devices(self):
        while self.running:
            current_temperature = self.zone_model.thermometer.get_value()
            current_air_humidity = self.zone_model.air_humidity_sensor.get_value()

            if callable(self.zone_model.heater.scale_device(1)):
                if current_temperature < self.zone_model.ideal_temperature:
                    self.zone_model.heater.scale_device(10)
                    self.zone_model.thermometer.raise_value(1)
                else:
                    self.zone_model.heater.scale_device(-100)

            if callable(self.zone_model.fan.scale_device(1)):
                if current_temperature > self.zone_model.ideal_temperature:
                    self.zone_model.fan.scale_device(10)
                    self.zone_model.thermometer.lower_value(1)
                    self.zone_model.air_humidity_sensor.lower_value(1)
                else:
                    self.zone_model.heater.scale_device(-100)
            if callable(self.zone_model.water_dispenser.dispense_water()):
                if current_air_humidity < self.zone_model.ideal_air_humidity:
                    self.zone_model.water_dispenser.dispense_water()
                    self.zone_model.air_humidity_sensor.raise_value(5)

            self.zone_model.air_humidity_sensor.random_value_change()
            time.sleep(10)
    def add_plant(self, name, i_soil_humidity):
        plant_controller = PlantFactory.create_plant(name, i_soil_humidity)
        self.zone_model.plants.append(plant_controller.plant_model)
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
