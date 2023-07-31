import threading
import time

from src.entities.layout.room.room_model import RoomModel
from src.utilities.log import Log


class RoomController:

    def __init__(self, room_model: RoomModel):
        self.room_model: RoomModel = room_model
        self.running = False
        self.thread = None

    def control_devices(self):
        while self.running:
            Log.write_to_log(str(self.room_model.name), 1)
            current_temperature = self.room_model.thermometer.get_value()
            current_air_humidity = self.room_model.air_humidity_sensor.get_value()


            if current_temperature < self.room_model.ideal_temperature:
                self.room_model.heater.scale_device(10)
                self.room_model.thermometer.raise_value(1)
            else:
                self.room_model.heater.scale_device(-100)


            if current_temperature > self.room_model.ideal_temperature:
                self.room_model.fan.scale_device(10)
                self.room_model.thermometer.lower_value(1)
                self.room_model.air_humidity_sensor.lower_value(1)
            else:
                self.room_model.heater.scale_device(-100)

            if current_air_humidity < self.room_model.ideal_air_humidity:
                self.room_model.water_dispenser.dispense_water()
                self.room_model.air_humidity_sensor.raise_value(5)

            self.room_model.air_humidity_sensor.random_value_change()
            time.sleep(10)
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
