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
        ]

        # dictionary for attribute to label text translation
        self.attribute_labels = {
            "name": "Name",
            "type": "Type",
            "temperature": "Temperature",
            "humidity": "Humidity",
        }

    def update_view_model(self, rooms, greenhouse_zones):
        self.rooms = rooms
        self.zones = greenhouse_zones

    def append_room(self, room: ZoneModel):
        self.rooms.append(room)

    def append_zone(self, zone: ZoneModel):
        self.zones.append(zone)
