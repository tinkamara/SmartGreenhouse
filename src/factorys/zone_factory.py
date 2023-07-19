
from src.model.places.greenhouse_model import Greenhouse


class ZoneFactory:

    @staticmethod
    def create_zone(greenhouse: Greenhouse, plant: str, ideal_temperature: int, ideal_air_humidity: int,
                    ideal_soil_humidity):

