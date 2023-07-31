from src.entities.devices.lamp.lamp_model import Lamp
from src.entities.devices.water_tank.water_tank_model import WaterTank
from src.entities.layout.greenhouse.greenhouse_model import GreenhouseModel
from src.entities.layout.zone.zone_model import ZoneModel
from src.factorys.zone_factory import ZoneFactory


class GreenhouseController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model: GreenhouseModel):
        self.greenhouse_model = model

    def add_zone(self, name, i_temp, i_air_humidity):
        # Überprüfen, ob der Zonenname bereits vorhanden ist
        if self.zone_name_exists(name):
            raise ValueError(f"A zone with the name '{name}' already exists.")

        # Eine neue Zone erstellen und zur Liste der Zonen hinzufügen
        zone_controller = ZoneFactory.create_zone(name, i_temp, i_air_humidity)
        self.greenhouse_model.zones.append(zone_controller.zone_model)

    def remove_zone(self, name):
        # Überprüfen, ob der Zonenname vorhanden ist
        zone = self.get_zone_by_name(name)
        if zone is None:
            raise ValueError(f"No zone with the name '{name}' found.")

        # Zone aus der Liste entfernen
        self.greenhouse_model.zones.remove(zone)

    def zone_name_exists(self, name):
        # Überprüfen, ob der Zonenname bereits vorhanden ist
        for zone in self.greenhouse_model.zones:
            if zone.name == name:
                return True
        return False

    def get_zone_by_name(self, name):
        # Eine Zone anhand des Namens suchen
        for zone in self.greenhouse_model.zones:
            if zone.name == name:
                return zone
        return None
