from src.entities.devices.fertilizer.fertilizer_model import FertilizerModel
from src.entities.devices.irrigation.irrigation_model import IrrigationModel
from src.entities.devices.uv_lamp.uv_lamp_model import UVLampModel
from src.entities.layout.greenhouse.greenhouse_model import GreenhouseModel
from src.entities.layout.plant.plant_controller import PlantController
from src.entities.layout.plant.plant_model import PlantModel
from src.entities.layout.zone.zone_model import ZoneModel
from src.entities.sensors.soil_humidity_sensor import SoilHumiditySensor


class PlantFactory:
    @staticmethod
    def create_plant(name: str, zone: ZoneModel, idealhumidity: int):
        soil_humidity_sensor = SoilHumiditySensor()
        uv_lamp = UVLampModel()
        fertilizer = FertilizerModel()
        irrigation = IrrigationModel()

        plant_model = PlantModel(name, zone, idealhumidity, soil_humidity_sensor, fertilizer, irrigation, uv_lamp)
        plant_controller: PlantController = PlantController(plant_model)
        plant_controller.start()
        return plant_controller






