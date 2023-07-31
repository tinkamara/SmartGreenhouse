import json
import time


class ConfigLoader:

    def __init__(self):
        self.filepath = "utilities/config.json"
        self.previous_data = None
        self.current_data = None

    def read_config(self):

        # Lese die Konfigurationsdatei zu Beginn
        with open(self.filepath) as rf:
            self.current_data = json.load(rf)
            return self.current_data

        # while True:
        #     with open(self.filepath) as rf:
        #         file_content = json.load(rf)
        #         self.current_data = file_content
        #
        #     # Vergleiche den aktuellen Inhalt mit dem gespeicherten Inhalt
        #     if self.current_data != self.previous_data:
        #         print("\nKonfigurationsänderungen:")
        #
        #         if self.previous_data is not None:
        #             self.compare_configurations()
        #
        #         # Aktualisiere den gespeicherten Inhalt mit dem aktuellen Inhalt
        #     self.previous_data = self.current_data.copy()
        #
        #     # Füge hier eine angemessene Wartezeit ein, bevor die nächste Iteration startet
        #     time.sleep(1)

    # def print_configuration(self):
    #     # Gib alle Informationen aus der Konfiguration aus
    #     for room in self.current_data["rooms"]:
    #         print(room["name"])
    #         for device in room["devices"]:
    #             print(f"\t{device['name']} <{device['type']}>")
    #
    #     for greenhouse_zone in self.current_data["greenhouse_zones"]:
    #         print(greenhouse_zone["name"])
    #         for device in greenhouse_zone["devices"]:
    #             print(f"\t{device['name']} <{device['type']}>")
    #         for plant in greenhouse_zone["plants"]:
    #             print(f"\t{plant['name']} <{plant['type']}>")
    #
    # def compare_configurations(self):
    #     # Vergleiche die Räume
    #
    #     # Vergleiche die Räume
    #     previous_rooms = {room["name"]: room for room in self.previous_data["rooms"]}
    #     current_rooms = {room["name"]: room for room in self.current_data["rooms"]}
    #
    #
    #     for room_name, current_room in current_rooms.items():
    #         previous_room = previous_rooms.get(room_name)
    #         if previous_room is None:
    #             print(f"Neuer Raum hinzugefügt: {room_name}")
    #         else:
    #             self.compare_devices(previous_room["devices"], current_room["devices"],
    #                                  f"Devices in Raum '{room_name}'")
    #
    #
    #     for room_name, previous_room in previous_rooms.items():
    #         if room_name not in current_rooms:
    #             print(f'Raum entfernt: {room_name}')
    #
    #     # Vergleiche die Gewächshauszonen
    #     previous_zones = {zone["name"]: zone for zone in self.previous_data["greenhouse_zones"]}
    #     current_zones = {zone["name"]: zone for zone in self.current_data["greenhouse_zones"]}
    #
    #     for zone_name, current_zone in current_zones.items():
    #         previous_zone = previous_zones.get(zone_name)
    #         if previous_zone is None:
    #             print(f"Neue Gewächshauszone hinzugefügt: {zone_name}")
    #         else:
    #             self.compare_devices(previous_zone["devices"], current_zone["devices"],
    #                                  f"Devices in Gewächshauszone '{zone_name}'")
    #             self.compare_plants(previous_zone["plants"], current_zone["plants"],
    #                                 f"Pflanzen in Gewächshauszone '{zone_name}'")
    #
    #     for zone_name, previous_zone in previous_zones.items():
    #         if zone_name not in current_zones:
    #             print(f"Gewächshauszone entfernt: {zone_name}")
    #
    # def compare_devices(self, previous_devices, current_devices, heading):
    #     previous_device_names = {device["name"] for device in previous_devices}
    #     current_device_names = {device["name"] for device in current_devices}
    #
    #     for device_name in current_device_names:
    #         if device_name not in previous_device_names:
    #             print(f"{heading}: Neues Gerät hinzugefügt: {device_name}")
    #
    #     for device_name in previous_device_names:
    #         if device_name not in current_device_names:
    #             print(f"{heading}: Gerät entfernt: {device_name}")
    #
    # def compare_plants(self, previous_plants, current_plants, heading):
    #     previous_plant_names = {plant["name"] for plant in previous_plants}
    #     current_plant_names = {plant["name"] for plant in current_plants}
    #
    #     for plant_name in current_plant_names:
    #         if plant_name not in previous_plant_names:
    #             print(f"{heading}: Neue Pflanze hinzugefügt: {plant_name}")
    #
    #     for plant_name in previous_plant_names:
    #         if plant_name not in current_plant_names:
    #             print(f"{heading}: Pflanze entfernt: {plant_name}")

#
# if __name__ == '__main__':
#     loader = ConfigLoader()
#     loader.read_config()
