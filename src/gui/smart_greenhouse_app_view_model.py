from src.entities.layout.zone.zone_model import ZoneModel


class SmartGreenhouseAppViewModel:

    def __init__(self, rooms, zones, hidden_attributes: []):
        self.rooms: [] = []
        self.zones: [] = []
        self.no_change_attributes = [
            "name",
            "type",
        ]

        # attributes to hide on auto-generated forms
        self.hidden_attributes = [
            "devices",
            "television",
            "heater",
            "fan",
            "uv_lamp",
            "lamp",
            "irrigation",
            "water_dispenser",
            "fertilizer",
            "plants",
            "water_tank",
            "zone"
        ]

        # dictionary for attribute to label text translation
        self.attribute_labels = {
            "name": "Name",
            "type": "Type",
            "ideal_temperature": "Idealtemperatur",
            "ideal_soil_humidity": "Ideale Bodenfeuchte",
            "ideal_air_humidity": "Ideale Luftfeuchtigkeit",
            "humidity": "Humidity",
            "air_humidity_sensor": "Aktuelle Luftfeuchtigkeit",
            "thermometer": "Aktuelle Temperatur",
            "soil_humidity_sensor": "Bodenfeuchtigkeit"
        }

    def update_view_model(self, rooms, greenhouse_zones):
        self.rooms = rooms
        self.zones = greenhouse_zones

    def append_room(self, room: ZoneModel):
        self.rooms.append(room)

    def append_zone(self, zone: ZoneModel):
        self.zones.append(zone)

    def remove_zone(self, zone_name):
        value_to_remove = zone_name
        index_to_remove = None
        for index, obj in enumerate(self.zones):
            if obj.name == value_to_remove:
                index_to_remove = index

        if index_to_remove is not None:
            self.zones.pop(index_to_remove)

    def remove_room(self, room_name):
        value_to_remove = room_name
        index_to_remove = None
        for index, obj in enumerate(self.rooms):
            if obj.name == value_to_remove:
                index_to_remove = index

        if index_to_remove is not None:
            self.rooms.pop(index_to_remove)

