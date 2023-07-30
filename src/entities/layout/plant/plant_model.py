from src.entities.devices.fertilizer.fertilizer_model import FertilizerModel
from src.entities.devices.irrigation.irrigation_model import IrrigationModel
from src.entities.devices.uv_lamp.uv_lamp_model import UVLampModel
from src.entities.layout.zone.zone_model import ZoneModel
from src.entities.sensors.soil_humidity_sensor import SoilHumiditySensor


class PlantModel:
    def __init__(self, name: str, zone: ZoneModel, ideal_soil_humidity: int, soil_humidity_sensor: SoilHumiditySensor, fertilizer: FertilizerModel,
                 irrigation: IrrigationModel, uv_lamp: UVLampModel):
        self.name = name
        self.zone = zone
        self.uv_lamp: UVLampModel = uv_lamp
        self.fertilizer: FertilizerModel = fertilizer
        self.irrigation: IrrigationModel = irrigation
        self.soil_humidity_sensor: SoilHumiditySensor = soil_humidity_sensor
        self.ideal_soil_humidity: int = ideal_soil_humidity

        # Methode zum Erhöhen der idealen Bodenfeuchtigkeit um einen bestimmten Wert
    def increase_ideal_soil_humidity(self, increment: int):
        self.ideal_soil_humidity += increment

        # Methode zum Verringern der idealen Bodenfeuchtigkeit um einen bestimmten Wert
    def decrease_ideal_soil_humidity(self, decrement: int):
        self.ideal_soil_humidity -= decrement
