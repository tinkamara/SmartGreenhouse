import threading
import time

from src.entities.layout.plant.plant_model import PlantModel
from src.exceptions.no_fertilizer_exception import NoFertilizerException
from src.utilities.FloraGPT import FloraGPT
from src.utilities.log import Log


class PlantController:

    def __init__(self, plant_model: PlantModel):
        self.plant_model = plant_model
        self.running = False
        self.thread = None

    def control_devices(self):
        while self.running:
            current_soil_humidity = self.plant_model.soil_humidity_sensor.get_value()

            if current_soil_humidity < self.plant_model.ideal_soil_humidity:
                self.plant_model.irrigation.water_plant()
                self.plant_model.soil_humidity_sensor.raise_value(10)
                Log.write_to_log(
                    str(self.plant_model.name) + " bewässert",
                    1)

            current_uv_scale = self.plant_model.uv_lamp.brightness

            if current_uv_scale != self.plant_model.uv_lamp_scale:
                self.plant_model.uv_lamp.brightness = self.plant_model.uv_lamp_scale
                Log.write_to_log(
                    "Helligkeit der UV-Lampe fuer " + str(self.plant_model.name) + " angepasst",
                    1)

            self.call_ai()

            self.plant_model.soil_humidity_sensor.random_value_change()
            self.plant_model.soil_humidity_sensor.lower_value(2)

            time.sleep(10)

    def call_ai(self):
        message = FloraGPT.ermittlePflegehinweis('Bild')
        if '001' in message:
            self.plant_model.increase_ideal_soil_humidity(5)
            Log.write_to_log(
                "Ideale Bodenfeuchtigkeit fuer " + str(self.plant_model.name) + " um 5% erhoeht",
                1)
        if '002' in message:
            self.plant_model.decrease_ideal_soil_humidity(5)
            Log.write_to_log(
                "Ideale Bodenfeuchtigkeit fuer " + str(self.plant_model.name) + " um 5% verringert",
                1)
        if '010' in message:
            try:
                self.plant_model.fertilizer.fertilize()
                Log.write_to_log(
                    str(self.plant_model.name) + " geduengt",
                    1)
            except NoFertilizerException as e:
                Log.write_to_log(e.message + " bei Planze " + str(self.plant_model.name))
        if '020' in message:
            self.plant_model.zone.increase_ideal_air_humidity(5)
            Log.write_to_log(
                "Ideale Luftfeuchtigkeit fuer " + str(self.plant_model.name) + " um 5% erhoeht",
                1)
        if '021' in message:
            self.plant_model.zone.decrease_ideal_air_humidity(5)
            Log.write_to_log(
                "Ideale Luftfeuchtigkeit fuer " + str(self.plant_model.name) + " um 5% verringert",
                1)
        if '030' in message:
                self.plant_model.increase_uv_lamp_scale(10)
        Log.write_to_log(
            "Ideale UV-Beleuchtung fuer " + str(self.plant_model.name) + " um 10% erhoeht",
            1)
        if '031' in message:
            self.plant_model.decrease_uv_lamp_scale(10)
            Log.write_to_log(
                "Ideale UV-Beleuchtung fuer " + str(self.plant_model.name) + " um 10% verringert",
                1)

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
